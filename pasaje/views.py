from datetime import date, datetime, timedelta
from itertools import chain
from django_q.tasks import async_task
from csv_export.views import CSVExportView
from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.db.models import CharField, Value, Q
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
    context_object_name = 'Tickets'
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

        colgados = Eventostkt.objects.values('sk','id','horario').filter(
            Q(estado = 'Asignado') | Q(estado = 'En Curso'),
            Q(grupo_asignado = 'SERVICE DESK') | Q(grupo_asignado = 'SERVICE INCIDENT RESOLUTION') | Q(grupo_asignado__icontains = 'UNIDAD OPERATIVA'),
            horario__range = (datetime.now()+timedelta(minutes=-120),datetime.now()+timedelta(minutes=-30))
            )
        

        id = []

        for i in list(colgados):
            id.append(i['id'])
     
        id = list(set(id))
        
        colgados = len(id)

        


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
                   'colgados':colgados
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

        #muestro aquellos tkt que esten en curso hace mas de 20 minutos y menos de 2 horas.
        colgados = Eventostkt.objects.values('sk','id').filter(
            Q(estado = 'Asignado') | Q(estado = 'En Curso'),
            Q(grupo_asignado = 'SERVICE DESK') | Q(grupo_asignado = 'SERVICE INCIDENT RESOLUTION') | Q(grupo_asignado__icontains = 'UNIDAD OPERATIVA'),
            horario__range = (datetime.now()+timedelta(minutes=-120),datetime.now()+timedelta(minutes=-30))
            )   
        
        eventos = Eventostkt.objects.values('sk','id')


        #Voy a crear una lista con los SK mas altos de cada tkt de la query colgados.
        borrar = []

        for i in list(colgados):
            a = 0
            for e in list(colgados):
                if i['id'] == e['id']:
                    if e['sk'] > i['sk']:
                        a = e
                else:
                    pass
            if a != 0:
                borrar.append(a)
        
        #elimino elementos repetidos de borrar y lo guardo en borrar2
        borrar2 = []

         #en borrar 2 ya no hay elementos repetidos
        [borrar2.append(x) for x in borrar if x not in borrar2] 
        

        #limpio borrar para crear una lista donde vere si en eventos hay SK mas 
        #altos para cada tkt.

        borrar = []
        
        for i in borrar2:
            a = 0
            for e in list(eventos):
                if i['id'] == e['id']:
                    if e['sk'] > i['sk']:
                        a = e
                    else:
                        pass

            if a != 0:
                borrar.append(a)

        #Ahora comparo borrar2 que tiene los reclamos de colgados y lo comparo con
        #borrar que tiene los SK mas altos para los tickets que aparecen en borrar2,
        #si no aparece en borrar2 significa que es el ultimo sk y por lo tanto aun no se movio.

        limpio = []

        [limpio.append(x) for x in borrar2 if x not in borrar] 
        



        if palabra_clave != '':
            lista = []
            celula = CsvImportado1.objects.values('id').filter(
               celula_n = palabra_clave,
               tipo_incidencia = 'User Service Restoration',
            )
            # creo lista con los id 
            for i in list(celula):
                lista.append(i)
            #comparo comparo solo los id de la lista id contra lista. Si esta en ambas crea una nueva lista llamada id
            limpio = [x for x in limpio if x in lista]
        else:
            pass 

        print('==============se ejecuto===================')
        for i in limpio:
            print(i['sk'])
        print('==============finalizo===================')

        
        sk = []
        for i in limpio:
            sk.append(i['sk'])


        colgados = Eventostkt.objects.values('sk','id','grupo_asignado','horario','estado').filter(
            sk__in = sk,
            )

        celulas = CsvImportado1.objects.values('id','celula_n')


        #pasados a resueltos en las ultimas 2 horas.



        context = {'colgados' : colgados,
                   'celulas' : celulas
                }

        return render(request,'colgados.html',context)