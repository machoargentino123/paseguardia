from datetime import date, datetime, timedelta
from itertools import chain
from django.db import connection
from django_q.tasks import async_task
from csv_export.views import CSVExportView
from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.db.models import CharField, Value, Q, Max, Value, Min
# Create your views here.
from django.views.generic import (TemplateView, 
                                  ListView, 
                                  CreateView, 
                                  DetailView, 
                                  CreateView, 
                                  UpdateView,
                                  DeleteView,)

from .models import (CsvImportado1,
                     CsvImportado2,
                     Tablaseguimiento,
                     Eventostkt,
                     Llamadas,
                     Llamadasssdd,)

from .forms import TktForm
from django.urls import reverse_lazy



"""
Async_task realiza tareas asincronas 
tiene:
modulo o funcion que va a ejecutar.
argumentos
hook, donde 
"""

#esta es llamada desde tasks.py y a su vez la llama el django-q desde el cluster
def imprimir():
    print("#####################")
    print("desde views")
    print("#####################")


class Asincrono():
    def index(request):
        json_payload = {
            "message" : "Hello World"
        }
        async_task("pasaje.tasks.sleep_and_print", 35, hook = "pasaje.tasks.after_sleeping")
        return JsonResponse(json_payload)


class Pruebagraficos():
    def index(request):

        cel1 = CsvImportado1.objects.filter(
            celula_n = 1
        ).count()

        cel2 = CsvImportado1.objects.filter(
            celula_n = 2
            ).count()

        cel3 = CsvImportado1.objects.filter(
            celula_n = 3
        ).count()

        cel4 = CsvImportado1.objects.filter(
            celula_n = 4
        ).count()
        

        colgados = Eventostkt.objects.values('id','grupo_asignado','horario','estado').filter( 
            Q(estado = 'Asignado') | Q(estado = 'En Curso'),
            horario__range = (datetime.now()-timedelta(minutes=20),datetime.now())  
            ).filter(
                Q(grupo_asignado = 'SERVICE DESK') | Q(grupo_asignado = 'SERVICE INCIDENT RESOLUTION') | Q(grupo_asignado__icontains = 'UNIDAD OPERATIVA')
            ).distinct()
    

          
        context = {'cel1' : cel1, 
                   'cel2' : cel2,
                   'cel3' : cel3,
                   'cel4' : cel4,
                   'colgados': colgados,
                   }
        return render(request,'graficos.html',context) 



#pagina de inicio
class InicioView(TemplateView):
    template_name = 'inicio.html'

#listado de todos los reclamos que hay.
class ListaView(ListView):
    context_object_name = 'Tickets'
    template_name = 'lista.html'
    paginate = 200
    uno = 2

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        if palabra_clave != '':
            lista = CsvImportado1.objects.filter(
                id__icontains = palabra_clave,
            ).filter( status_reason_hidden__icontains = 'Monitoring Incident')
            return lista
        else:
            return CsvImportado1.objects.all() 




#Pagina de los reclamos para seguimiento
class ListaView2(ListView):
    context_object_name = 'lista'
    template_name = 'guardia.html'
    paginate = 200
   
    def get_queryset(self):
        
        palabra_clave = self.request.GET.get('kword', '')

        if palabra_clave == 'filtrar':
            lista = Tablaseguimiento.objects.filter(
                detalle = 'Actualizar',
            ).order_by(
                'tkt__grupo_asignado',
                'detalle'
            )
            return lista
        elif palabra_clave != '':
            lista = Tablaseguimiento.objects.filter(
                tkt__celula_n = palabra_clave,
            ).order_by(
                'tkt__grupo_asignado',
                'detalle'
            )
            return lista
        else:
            lista = Tablaseguimiento.objects.all().order_by(
                'tkt__grupo_asignado',
                'detalle'
            )
            print(type(lista[0]))
            return lista
    



#vista para editar los reclamos. 

class ActualizarTkt(UpdateView):
    model = Tablaseguimiento
    template_name = "actualizar.html"
    fields = ['detalle', 'reactivar','reactivar_hora', 'prioridad']  
    success_url = reverse_lazy('pasaje_app:Guardia')

    #GUARDAR DESPUES DE VALIDAR

    def form_valid(self,form):
        #logica de la funcion.
        return super(ActualizarTkt,self).form_valid(form)


#vista Que tiene una query cruda, porque django no permite
#hacer joins sin foreighn keys
class ListaView3():
   
    def index(request):
        x = []

        lista1 = CsvImportado1.objects.all()
        lista2 = CsvImportado2.objects.all()
        fecha = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        for a in lista1:
            for b in lista2:
                if a.id == b.id: 
                    if a.grupo_asignado != b.grupo_asignado:
                        x.append(a.id)
                    elif a.estado != b.estado:
                        x.append(a.id)
                    else:
                        pass
        

        lista = CsvImportado1.objects.filter(id__in = x).extra(
            select = {'bandeja_anterior':'CSV_Importado2.grupo_asignado',
                      'estado_anterior':'CSV_Importado2.Estado',
                      'status_anterior':'CSV_Importado2.Status_Reason_Hidden',
                    },
            tables = ['CSV_Importado1','CSV_Importado2'],
            where = ['CSV_Importado1.id = CSV_Importado2.id']
         ).values('id','grupo_asignado','estado','status_reason_hidden','bandeja_anterior','estado_anterior','status_anterior')


        lista = lista.annotate(fecha_hora=Value(fecha, output_field=CharField()))
        for i in lista:
            print(i)
    


        context = {'lista':lista,
                   'fecha' : fecha,
                  } 

        return render(request,'celula.html',context)


#vista Test 2  visualizar los eventos en la tabla eventostkt

class eventos(ListView):
    context_object_name = 'lista'
    template_name = 'lista.html'
    paginate = 500

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        if palabra_clave != '':
     
            lista = Eventostkt.objects.filter(
                    id__icontains = palabra_clave   
                    )
            

            return lista
        else:
            #return Eventostkt.objects.values('id').annotate(sk=Max('sk'))
            return Eventostkt.objects.all()


#exporta todo a CSV 
class ExportCSVAll(CSVExportView):

    fields = ('tkt__id',
              'tkt__celula_n',
              'tkt__grupo_asignado',
              'tkt__razon_social',
              'tkt__ci',
              'tkt__status_reason_hidden',
              'reactivar',
              'reactivar_hora',
              'prioridad',
              'detalle',
              )
    specify_separator = False
    filename = 'data-export.csv'

    def get_queryset(self):
        queryset = Tablaseguimiento.objects.select_related().all()
        return queryset
#Exporta a CSV lo de la celula 1
class ExportCSVCel1(CSVExportView):

    def __init__(self):
        self.grupo = 1

    fields = ('tkt__id',
              'tkt__celula_n',
              'tkt__grupo_asignado',
              'tkt__razon_social',
              'tkt__ci',
              'tkt__status_reason_hidden',
              'reactivar',
              'reactivar_hora',
              'prioridad',
              'detalle',
              )
    specify_separator = False
    filename = 'data-export.csv'

    def get_queryset(self):
        queryset = Tablaseguimiento.objects.select_related().filter(
            tkt__celula_n = self.grupo
        )
        return queryset
#Exporta a CSV lo de la celula 2
class ExportCSVCel2(CSVExportView):
    def __init__(self):
        self.grupo = 2

    fields = ('tkt__id',
              'tkt__celula_n',
              'tkt__grupo_asignado',
              'tkt__razon_social',
              'tkt__ci',
              'tkt__status_reason_hidden',
              'reactivar',
              'reactivar_hora',
              'prioridad',
              'detalle',
              )
    specify_separator = False
    filename = 'data-export.csv'

    def get_queryset(self):
        queryset = Tablaseguimiento.objects.select_related().filter(
            tkt__celula_n = self.grupo
        )
        return queryset
#Exporta a CSV lo de la celula 3
class ExportCSVCel3(CSVExportView):
    def __init__(self):
        self.grupo = 3

    fields = ('tkt__id',
              'tkt__celula_n',
              'tkt__grupo_asignado',
              'tkt__razon_social',
              'tkt__ci',
              'tkt__status_reason_hidden',
              'reactivar',
              'reactivar_hora',
              'prioridad',
              'detalle',
              )
    specify_separator = False
    filename = 'data-export.csv'

    def get_queryset(self):
        queryset = Tablaseguimiento.objects.select_related().filter(
            tkt__celula_n = self.grupo
        )
        return queryset
#Exporta a CSV lo de la celula 4
class ExportCSVCel4(CSVExportView):
    def __init__(self):
        self.grupo = 4

    fields = ('tkt__id',
              'tkt__celula_n',
              'tkt__grupo_asignado',
              'tkt__razon_social',
              'tkt__ci',
              'tkt__status_reason_hidden',
              'reactivar',
              'reactivar_hora',
              'prioridad',
              'detalle',
              )
    specify_separator = False
    filename = 'data-export.csv'

    def get_queryset(self):
        print(self.grupo)
        queryset = Tablaseguimiento.objects.select_related().filter(
            tkt__celula_n = self.grupo
        )
        return queryset

#vista del panel de monitoreo.
class PanelMonitoreo():

    def index(request):
        total = CsvImportado1.objects.count()

        cel1 = CsvImportado1.objects.filter(
            celula_n = 1
        ).count()

        cel2 = CsvImportado1.objects.filter(
            celula_n = 2
            ).count()

        cel3 = CsvImportado1.objects.filter(
            celula_n = 3
        ).count()

        cel4 = CsvImportado1.objects.filter(
            celula_n = 4
        ).count()


        cela1 = CsvImportado1.objects.filter(
            celula_n = 1,
            tipo_incidencia = 'User Service Restoration',
            ).count()

        cela2 = CsvImportado1.objects.filter(
            celula_n = 2,
            tipo_incidencia = 'User Service Restoration',
            ).count()
        
        cela3 = CsvImportado1.objects.filter(
            celula_n = 3,
            tipo_incidencia = 'User Service Restoration',
             ).count()
            
        cela4 = CsvImportado1.objects.filter(
            celula_n = 4,
            tipo_incidencia = 'User Service Restoration',
            ).count()


        fecha = datetime.now()

        valor = request.GET.get('kword', '')
        if valor == '':
            valor = 'sin valor'
        
        llamadas_md = Llamadas.objects.using('avaya').all()
        
        llamadas_sd = Llamadasssdd.objects.using('avaya').all()

        # Listo los colgados que estan en curso desde hace 120 minutos

        with connection.cursor() as cursor:
            cursor.execute("SELECT ID, max(sk) AS sk ,min(Horario) AS horario FROM `eventostkt` GROUP BY ID")
            colgados = cursor.fetchall()

        sklist = []

        for i in list(colgados):
            sklist.append(i[1])

        colgados = Eventostkt.objects.values('sk','id','grupo_asignado','horario','estado').filter(
            sk__in = sklist
            ).filter(
            Q(estado = 'Asignado') | Q(estado = 'En Curso'),
            Q(grupo_asignado = 'SERVICE DESK') | Q(grupo_asignado = 'SERVICE INCIDENT RESOLUTION') | Q(grupo_asignado__icontains = 'UNIDAD OPERATIVA'),
            tipo_incidencia = 'User Service Restoration',
            horario__range = (datetime.now()+timedelta(minutes=-180),datetime.now()+timedelta(minutes=-30))
            ).count()
        

        resueltos = Eventostkt.objects.values('sk','id','grupo_asignado','grupo_asignado_anterior','horario','estado').filter(
                sk__in = sklist
                ).filter(
                    estado = 'Resolved',
                ).filter(
                    Q(grupo_asignado_anterior__icontains = 'OPERACION') | Q(grupo_asignado_anterior__icontains = 'OP TRANSITO') | Q(grupo_asignado_anterior__icontains = 'AOP') | Q(grupo_asignado_anterior = 'GRIP') | Q(grupo_asignado_anterior = 'SECURITY OPERATION CENTER') | Q(grupo_asignado_anterior__icontains = 'NOA') | Q(grupo_asignado_anterior__icontains = 'NEA'),
                    horario__range = (datetime.now()+timedelta(minutes=-90),datetime.now())
                ).count()



        context = {'total': total, 
                   'cel1' : cel1,
                   'cel2' : cel2,
                   'cel3' : cel3,
                   'cel4' : cel4,
                   'cela1' : cela1,
                   'cela2' : cela2,
                   'cela3' : cela3,
                   'cela4' : cela4,
                   'fecha': fecha,
                   'valor': valor,
                   'llamadas_md':llamadas_md,
                   'llamadas_sd':llamadas_sd,
                   'colgados':colgados,
                   'resueltos': resueltos
                   }

        return render(request,'panel.html',context) 

#Lista los reclamos de cada celula labura en conjunto con la vista panel monitoreo
class ListarCel(ListView):
    context_object_name = 'lista'
    template_name = 'celula.html'
    paginate = 200
   
    def get_queryset(self):
        valor =self.kwargs['pk'] # recupera el dato del PK.
        lista = CsvImportado1.objects.filter(
               celula_n = valor, 
            )
        return lista


#listar reclamos colgados de + de 20 minutos.
class ListarColgados():



    def index(request):


        palabra_clave = request.GET.get('kword', '')
        start = datetime.now()+timedelta(minutes=-180)
        end = datetime.now()+timedelta(minutes=-30)
        #muestro aquellos tkt que esten en curso hace mas de 20 minutos y menos de 2 horas.

        with connection.cursor() as cursor:
            cursor.execute("SELECT ID, max(sk) AS sk ,min(Horario) AS horario FROM `eventostkt` GROUP BY ID")
            colgados = cursor.fetchall()


        limpio = list(colgados)


        if palabra_clave != '':
            lista = []

            celula = CsvImportado1.objects.values('id').filter(
               celula_n = palabra_clave,
               tipo_incidencia = 'User Service Restoration',
            )
            # creo lista con los id 
            
            for i in limpio:
                a = 0
                for e in list(celula):
                    if i[0] == e['id']:
                        a = i
                    else:
                        pass
                if a != 0:
                    lista.append(a)
            
            limpio = []
            #Saco los repetidos
            [limpio.append(x) for x in lista if x not in limpio]
        
        else: 
            pass
            
        sklist = []
        for i in limpio:
            sklist.append(i[1])

        colgados = Eventostkt.objects.values('sk','id','grupo_asignado','horario','estado').filter(
            sk__in = sklist
            ).filter(
            Q(estado = 'Asignado') | Q(estado = 'En Curso'),
            Q(grupo_asignado = 'SERVICE DESK') | Q(grupo_asignado = 'SERVICE INCIDENT RESOLUTION') | Q(grupo_asignado__icontains = 'UNIDAD OPERATIVA'),
            tipo_incidencia = 'User Service Restoration',
            horario__range = (start,end)
            )


        celulas = CsvImportado1.objects.values('id','celula_n')


        #pasados a resueltos en las ultimas 2 horas.



        context = {'colgados' : colgados,
                   'celulas' : celulas
                }

        return render(request,'colgados.html',context)

#lista los resueltos.


class ListarDevueltos():

    def index(request):
        palabra_clave = request.GET.get('kword', '')

        start = datetime.now()+timedelta(minutes=-90)
        end = datetime.now()
        
        with connection.cursor() as cursor:
            cursor.execute("SELECT ID, max(sk) AS sk FROM `eventostkt` GROUP BY ID")
            ultimos = cursor.fetchall()
        

        if palabra_clave != '':
            print('Palabras clave', palabra_clave)
            celula = CsvImportado1.objects.values('id').filter(
               celula_n = palabra_clave,
            )   

            lista = []
            for i in ultimos:
                a = 0
                for e in list(celula):
                    if i[0] == e['id']:
                        a = i
                    else:
                        pass
                if a != 0:
                    lista.append(a)

            ultimos = []

            [ultimos.append(x) for x in lista if x not in ultimos]

            
        else:
            pass

        print('Tamaño de ultimos',len(ultimos))
        
        sklist = []
        
        for i in ultimos:
            sklist.append(i[1])

        ultimos = Eventostkt.objects.values('sk','id','grupo_asignado','grupo_asignado_anterior','horario','estado').filter(
                sk__in = sklist
                ).filter(
                    estado = 'Resolved',
                ).filter(
                    Q(grupo_asignado_anterior__icontains = 'OPERACION') | Q(grupo_asignado_anterior__icontains = 'OP TRANSITO') | Q(grupo_asignado_anterior__icontains = 'AOP') | Q(grupo_asignado_anterior = 'GRIP') | Q(grupo_asignado_anterior = 'SECURITY OPERATION CENTER') | Q(grupo_asignado_anterior__icontains = 'NOA') | Q(grupo_asignado_anterior__icontains = 'NEA')| Q(grupo_asignado_anterior__icontains = 'NEA')| Q(grupo_asignado_anterior__icontains = 'RED') | Q(grupo_asignado_anterior__icontains = 'OPER BACKBONE') | Q(grupo_asignado_anterior__icontains = 'OPERCLIENTE') | Q(grupo_asignado_anterior = 'GESTION PABX'), 
                    horario__range = (start,end)
                )

        celulas = CsvImportado1.objects.values('id','celula_n')

        context = {
            'colgados' : ultimos,
            'celulas' : celulas
        }

        return render(request,'resueltos.html',context)