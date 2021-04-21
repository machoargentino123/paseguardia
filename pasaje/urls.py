from django.contrib import admin
from django.urls import path
from . import views

app_name = 'pasaje_app'

urlpatterns = [
    path('',views.InicioView.as_view(), name= "Inicio"),
    path('listar/',views.ListaView.as_view(), name= "Listar"),
    path('guardia/',views.ListaView2.as_view(), name= "Guardia"),
    path('celula/',views.ListaView3.index, name="celula"),
    path('eventos/',views.eventos.as_view(), name="eventos"),
    path('actualizar/<pk>',views.ActualizarTkt.as_view(), name="actualizar"),
    path('hola/',views.PruebaView.index, name="hola"),
    path('hola2/',views.Asincrono.index, name="hola2"),
    path('csvall/',views.ExportCSVAll.as_view(), name="csvall"),
    path('csv1/',views.ExportCSVCel1.as_view(), name="csv1"),
    path('csv2/',views.ExportCSVCel2.as_view(), name="csv2"),
    path('csv3/',views.ExportCSVCel3.as_view(), name="csv3"),
    path('csv4/',views.ExportCSVCel4.as_view(), name="csv4"),
    path('panel/',views.PanelMonitoreo.index, name="panel"),
    path('graficos/',views.Pruebagraficos.index, name= "graficos"),
    
]   
