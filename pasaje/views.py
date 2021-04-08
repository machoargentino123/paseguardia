from datetime import date, datetime
from itertools import chain
from django_q.tasks import async_task
from csv_export.views import CSVExportView
from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.db.models import OuterRef, Subquery
from django.db.models.functions import TruncDate
# Create your views here.
from django.views.generic import (TemplateView, 
                                  ListView, 
                                  CreateView, 
                                  DetailView, 
                                  CreateView, 
                                  UpdateView,
                                  DeleteView)

from .models import (CsvImportado1,
                     CsvImportado2,
                     CsvImportado3,
                     CsvImportado4,
                     CsvImportado5,
                     CsvImportado6,
                     CsvImportado7,
                     CsvImportado8,
                     CsvImportado9,
                     CsvImportado10,
                     Tablaseguimiento)

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



class PruebaView():

    def index(request):

        lista = Tablaseguimiento.objects.all()
        fecha = date.today()
        valor = 3
        context = {'lista' : lista, 
                   'fecha' : fecha,
                   'valor' : valor,
                   }
        return render(request,'hola.html',context) 

#pagina de inicio
class InicioView(TemplateView):
    template_name = 'inicio.html'

#listado de todos los reclamos que hay.
class ListaView(ListView):
    context_object_name = 'Tickets'
    template_name = 'lista.html'
    paginate = 20
    uno = 2

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        if palabra_clave != '':
            lista = CsvImportado1.objects.filter(
                celula_n__icontains = palabra_clave,
            ).filter( status_reason_hidden__icontains = 'Monitoring Incident')
            return lista
        else:
            return CsvImportado1.objects.all() 

#listado de reclamos que hay
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
    
#vista para visualizar los reclamos de todas las celulas. No esta linkeado a nada, pero anda
#  
class ListaView3():
   
    def index(request):
        x = []
        lista1 = CsvImportado1.objects.all()
        lista2 = CsvImportado2.objects.all()
        lista3 = CsvImportado3.objects.all().values('id','grupo_asignado','estado','status_reason_hidden','tipo_incidencia')
        lista4 = CsvImportado4.objects.all().values('id','grupo_asignado','estado','status_reason_hidden','tipo_incidencia')
        lista5 = CsvImportado5.objects.all().values('id','grupo_asignado','estado','status_reason_hidden','tipo_incidencia')
        lista6 = CsvImportado6.objects.all().values('id','grupo_asignado','estado','status_reason_hidden','tipo_incidencia')
        lista7 = CsvImportado7.objects.all().values('id','grupo_asignado','estado','status_reason_hidden','tipo_incidencia')
        lista8 = CsvImportado8.objects.all().values('id','grupo_asignado','estado','status_reason_hidden','tipo_incidencia')
        lista9 = CsvImportado9.objects.all().values('id','grupo_asignado','estado','status_reason_hidden','tipo_incidencia')
        lista10 = CsvImportado9.objects.all().values('id','grupo_asignado','estado','status_reason_hidden','tipo_incidencia')
        #listapreuba = CsvImportado1.objects.all().annotate()
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        for a in lista1:
            for b in lista2:
                if a.id == b.id: 
                    if a.grupo_asignado != b.grupo_asignado:
                        x.append(a.id)
                    elif a.estado != b.estado:
                        x.append(a.id)
                    else:
                        pass
        
        #el id__in acepta como parametro una lista
        #listaa = CsvImportado1.objects.filter(id__in = x).values('id','grupo_asignado','estado','status_reason_hidden','tipo_incidencia')
        lista = CsvImportado1.objects.filter(id__in = x).extra(
            select = {'bandeja_anterior':'CSV_Importado2.grupo_asignado'},
            tables = ['CSV_Importado1','CSV_Importado2'],
            where = ['CSV_Importado1.id = CSV_Importado2.id']
        ).values('id','grupo_asignado','bandeja_anterior','status_reason_hidden').annotate(fecha_hora = fecha)
        
        for i in lista:
            print(i)
                # print(i.id)
                # print(i.grupo_asignado)
                # print(i.bandeja_anterior)
                # print(i.status_reason_hidden)

        context = {'lista':lista,
                   'fecha' : fecha,
                  } 

        return render(request,'celula.html',context)

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
        

class PruebaView():

    def index(request):
        lista = Tablaseguimiento.objects.all()
        fecha = date.today()
        valor = 4
        context = {'lista' : lista, 
                   'fecha' : fecha,
                   'valor' : valor,
                   }
        return render(request,'hola.html',context) 



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
                   }


        return render(request,'panel.html',context) 
