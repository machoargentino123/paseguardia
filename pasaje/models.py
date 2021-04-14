from datetime import date
from django.db import models
from django.db.models.signals import post_save,post_delete
# Create your models here.

from .signals import prueba_signals, prueba_signals2

class CsvImportado1(models.Model):
    id = models.TextField(db_column='ID',primary_key=True)  # Field name made lowercase.
    grupo_asignado = models.TextField(db_column='Grupo_Asignado')  # Field name made lowercase. 
    estado = models.TextField(db_column='Estado')  # Field name made lowercase.
    status_reason_hidden = models.TextField(db_column='Status_Reason_Hidden')  # Field name made lowercase.
    id_cliente = models.TextField(db_column='ID_Cliente')  # Field name made lowercase.
    razon_social = models.TextField(db_column='Razon_Social')  # Field name made lowercase.
    cliente_sidi = models.TextField(db_column='Cliente_SIDI')  # Field name made lowercase.
    ci = models.TextField(db_column='CI')  # Field name made lowercase.
    clase_ci = models.TextField(db_column='CLASE_CI')  # Field name made lowercase.
    fecha_envio = models.TextField(db_column='Fecha_Envio')  # Field name made lowercase.
    tipo_incidencia = models.TextField(db_column='Tipo_Incidencia')  # Field name made lowercase.
    segmento = models.TextField(db_column='Segmento')  # Field name made lowercase.
    n2_categ_prod = models.TextField(db_column='N2_Categ_Prod')  # Field name made lowercase.
    n3_categ_prod = models.TextField(db_column='N3_Categ_Prod')  # Field name made lowercase.
    n1_cat_ope = models.TextField(db_column='N1_Cat_Ope')  # Field name made lowercase.
    n2_cat_ope = models.TextField(db_column='N2_Cat_Ope')  # Field name made lowercase. 
    n3_cat_ope = models.TextField(db_column='N3_Cat_Ope')  # Field name made lowercase.
    urgencia = models.TextField(db_column='Urgencia')  # Field name made lowercase.
    prioridad = models.TextField(db_column='Prioridad')  # Field name made lowercase. 
    fecha_cierre = models.TextField(db_column='Fecha_Cierre')  # Field name made lowercase.
    assigned_company = models.TextField(db_column='Assigned_Company')  # Field name made lowercase.
    assigned_org = models.TextField(db_column='Assigned_Org')  # Field name made lowercase.
    usuario_asignado = models.TextField(db_column='Usuario_Asignado')  # Field name made lowercase.
    remitente = models.TextField(db_column='Remitente')  # Field name made lowercase.
    ultima_mod = models.TextField(db_column='Ultima_Mod')  # Field name made lowercase.
    celula_n = models.IntegerField(db_column='Celula_N')  # Field name made lowercase.        

    class Meta:
        managed = True
        db_table = 'CSV_Importado1' 

class CsvImportado2(models.Model):
    id = models.TextField(db_column='ID',primary_key=True)  # Field name made lowercase.
    grupo_asignado = models.TextField(db_column='Grupo_Asignado')  # Field name made lowercase. 
    estado = models.TextField(db_column='Estado')  # Field name made lowercase.
    status_reason_hidden = models.TextField(db_column='Status_Reason_Hidden')  # Field name made lowercase.
    id_cliente = models.TextField(db_column='ID_Cliente')  # Field name made lowercase.
    razon_social = models.TextField(db_column='Razon_Social')  # Field name made lowercase.
    cliente_sidi = models.TextField(db_column='Cliente_SIDI')  # Field name made lowercase.
    ci = models.TextField(db_column='CI')  # Field name made lowercase.
    clase_ci = models.TextField(db_column='CLASE_CI')  # Field name made lowercase.
    fecha_envio = models.TextField(db_column='Fecha_Envio')  # Field name made lowercase.
    tipo_incidencia = models.TextField(db_column='Tipo_Incidencia')  # Field name made lowercase.
    segmento = models.TextField(db_column='Segmento')  # Field name made lowercase.
    n2_categ_prod = models.TextField(db_column='N2_Categ_Prod')  # Field name made lowercase.
    n3_categ_prod = models.TextField(db_column='N3_Categ_Prod')  # Field name made lowercase.
    n1_cat_ope = models.TextField(db_column='N1_Cat_Ope')  # Field name made lowercase.
    n2_cat_ope = models.TextField(db_column='N2_Cat_Ope')  # Field name made lowercase. 
    n3_cat_ope = models.TextField(db_column='N3_Cat_Ope')  # Field name made lowercase.
    urgencia = models.TextField(db_column='Urgencia')  # Field name made lowercase.
    prioridad = models.TextField(db_column='Prioridad')  # Field name made lowercase. 
    fecha_cierre = models.TextField(db_column='Fecha_Cierre')  # Field name made lowercase.
    assigned_company = models.TextField(db_column='Assigned_Company')  # Field name made lowercase.
    assigned_org = models.TextField(db_column='Assigned_Org')  # Field name made lowercase.
    usuario_asignado = models.TextField(db_column='Usuario_Asignado')  # Field name made lowercase.
    remitente = models.TextField(db_column='Remitente')  # Field name made lowercase.
    ultima_mod = models.TextField(db_column='Ultima_Mod')  # Field name made lowercase.
    celula_n = models.IntegerField(db_column='Celula_N')  # Field name made lowercase.        

    class Meta:
        managed = True
        db_table = 'CSV_Importado2' 

class CsvImportado3(models.Model):
    id = models.TextField(db_column='ID',primary_key=True)  # Field name made lowercase.
    grupo_asignado = models.TextField(db_column='Grupo_Asignado')  # Field name made lowercase. 
    estado = models.TextField(db_column='Estado')  # Field name made lowercase.
    status_reason_hidden = models.TextField(db_column='Status_Reason_Hidden')  # Field name made lowercase.
    id_cliente = models.TextField(db_column='ID_Cliente')  # Field name made lowercase.
    razon_social = models.TextField(db_column='Razon_Social')  # Field name made lowercase.
    cliente_sidi = models.TextField(db_column='Cliente_SIDI')  # Field name made lowercase.
    ci = models.TextField(db_column='CI')  # Field name made lowercase.
    clase_ci = models.TextField(db_column='CLASE_CI')  # Field name made lowercase.
    fecha_envio = models.TextField(db_column='Fecha_Envio')  # Field name made lowercase.
    tipo_incidencia = models.TextField(db_column='Tipo_Incidencia')  # Field name made lowercase.
    segmento = models.TextField(db_column='Segmento')  # Field name made lowercase.
    n2_categ_prod = models.TextField(db_column='N2_Categ_Prod')  # Field name made lowercase.
    n3_categ_prod = models.TextField(db_column='N3_Categ_Prod')  # Field name made lowercase.
    n1_cat_ope = models.TextField(db_column='N1_Cat_Ope')  # Field name made lowercase.
    n2_cat_ope = models.TextField(db_column='N2_Cat_Ope')  # Field name made lowercase. 
    n3_cat_ope = models.TextField(db_column='N3_Cat_Ope')  # Field name made lowercase.
    urgencia = models.TextField(db_column='Urgencia')  # Field name made lowercase.
    prioridad = models.TextField(db_column='Prioridad')  # Field name made lowercase. 
    fecha_cierre = models.TextField(db_column='Fecha_Cierre')  # Field name made lowercase.
    assigned_company = models.TextField(db_column='Assigned_Company')  # Field name made lowercase.
    assigned_org = models.TextField(db_column='Assigned_Org')  # Field name made lowercase.
    usuario_asignado = models.TextField(db_column='Usuario_Asignado')  # Field name made lowercase.
    remitente = models.TextField(db_column='Remitente')  # Field name made lowercase.
    ultima_mod = models.TextField(db_column='Ultima_Mod')  # Field name made lowercase.
    celula_n = models.IntegerField(db_column='Celula_N')  # Field name made lowercase.        

    class Meta:
        managed = True
        db_table = 'CSV_Importado3'

class CsvImportado4(models.Model):
    id = models.TextField(db_column='ID',primary_key=True)  # Field name made lowercase.
    grupo_asignado = models.TextField(db_column='Grupo_Asignado')  # Field name made lowercase. 
    estado = models.TextField(db_column='Estado')  # Field name made lowercase.
    status_reason_hidden = models.TextField(db_column='Status_Reason_Hidden')  # Field name made lowercase.
    id_cliente = models.TextField(db_column='ID_Cliente')  # Field name made lowercase.
    razon_social = models.TextField(db_column='Razon_Social')  # Field name made lowercase.
    cliente_sidi = models.TextField(db_column='Cliente_SIDI')  # Field name made lowercase.
    ci = models.TextField(db_column='CI')  # Field name made lowercase.
    clase_ci = models.TextField(db_column='CLASE_CI')  # Field name made lowercase.
    fecha_envio = models.TextField(db_column='Fecha_Envio')  # Field name made lowercase.
    tipo_incidencia = models.TextField(db_column='Tipo_Incidencia')  # Field name made lowercase.
    segmento = models.TextField(db_column='Segmento')  # Field name made lowercase.
    n2_categ_prod = models.TextField(db_column='N2_Categ_Prod')  # Field name made lowercase.
    n3_categ_prod = models.TextField(db_column='N3_Categ_Prod')  # Field name made lowercase.
    n1_cat_ope = models.TextField(db_column='N1_Cat_Ope')  # Field name made lowercase.
    n2_cat_ope = models.TextField(db_column='N2_Cat_Ope')  # Field name made lowercase. 
    n3_cat_ope = models.TextField(db_column='N3_Cat_Ope')  # Field name made lowercase.
    urgencia = models.TextField(db_column='Urgencia')  # Field name made lowercase.
    prioridad = models.TextField(db_column='Prioridad')  # Field name made lowercase. 
    fecha_cierre = models.TextField(db_column='Fecha_Cierre')  # Field name made lowercase.
    assigned_company = models.TextField(db_column='Assigned_Company')  # Field name made lowercase.
    assigned_org = models.TextField(db_column='Assigned_Org')  # Field name made lowercase.
    usuario_asignado = models.TextField(db_column='Usuario_Asignado')  # Field name made lowercase.
    remitente = models.TextField(db_column='Remitente')  # Field name made lowercase.
    ultima_mod = models.TextField(db_column='Ultima_Mod')  # Field name made lowercase.
    celula_n = models.IntegerField(db_column='Celula_N')  # Field name made lowercase.        

    class Meta:
        managed = True
        db_table = 'CSV_Importado4'

class CsvImportado5(models.Model):
    id = models.TextField(db_column='ID',primary_key=True)  # Field name made lowercase.
    grupo_asignado = models.TextField(db_column='Grupo_Asignado')  # Field name made lowercase. 
    estado = models.TextField(db_column='Estado')  # Field name made lowercase.
    status_reason_hidden = models.TextField(db_column='Status_Reason_Hidden')  # Field name made lowercase.
    id_cliente = models.TextField(db_column='ID_Cliente')  # Field name made lowercase.
    razon_social = models.TextField(db_column='Razon_Social')  # Field name made lowercase.
    cliente_sidi = models.TextField(db_column='Cliente_SIDI')  # Field name made lowercase.
    ci = models.TextField(db_column='CI')  # Field name made lowercase.
    clase_ci = models.TextField(db_column='CLASE_CI')  # Field name made lowercase.
    fecha_envio = models.TextField(db_column='Fecha_Envio')  # Field name made lowercase.
    tipo_incidencia = models.TextField(db_column='Tipo_Incidencia')  # Field name made lowercase.
    segmento = models.TextField(db_column='Segmento')  # Field name made lowercase.
    n2_categ_prod = models.TextField(db_column='N2_Categ_Prod')  # Field name made lowercase.
    n3_categ_prod = models.TextField(db_column='N3_Categ_Prod')  # Field name made lowercase.
    n1_cat_ope = models.TextField(db_column='N1_Cat_Ope')  # Field name made lowercase.
    n2_cat_ope = models.TextField(db_column='N2_Cat_Ope')  # Field name made lowercase. 
    n3_cat_ope = models.TextField(db_column='N3_Cat_Ope')  # Field name made lowercase.
    urgencia = models.TextField(db_column='Urgencia')  # Field name made lowercase.
    prioridad = models.TextField(db_column='Prioridad')  # Field name made lowercase. 
    fecha_cierre = models.TextField(db_column='Fecha_Cierre')  # Field name made lowercase.
    assigned_company = models.TextField(db_column='Assigned_Company')  # Field name made lowercase.
    assigned_org = models.TextField(db_column='Assigned_Org')  # Field name made lowercase.
    usuario_asignado = models.TextField(db_column='Usuario_Asignado')  # Field name made lowercase.
    remitente = models.TextField(db_column='Remitente')  # Field name made lowercase.
    ultima_mod = models.TextField(db_column='Ultima_Mod')  # Field name made lowercase.
    celula_n = models.IntegerField(db_column='Celula_N')  # Field name made lowercase.        

    class Meta:
        managed = True
        db_table = 'CSV_Importado5'

class CsvImportado6(models.Model):
    id = models.TextField(db_column='ID',primary_key=True)  # Field name made lowercase.
    grupo_asignado = models.TextField(db_column='Grupo_Asignado')  # Field name made lowercase. 
    estado = models.TextField(db_column='Estado')  # Field name made lowercase.
    status_reason_hidden = models.TextField(db_column='Status_Reason_Hidden')  # Field name made lowercase.
    id_cliente = models.TextField(db_column='ID_Cliente')  # Field name made lowercase.
    razon_social = models.TextField(db_column='Razon_Social')  # Field name made lowercase.
    cliente_sidi = models.TextField(db_column='Cliente_SIDI')  # Field name made lowercase.
    ci = models.TextField(db_column='CI')  # Field name made lowercase.
    clase_ci = models.TextField(db_column='CLASE_CI')  # Field name made lowercase.
    fecha_envio = models.TextField(db_column='Fecha_Envio')  # Field name made lowercase.
    tipo_incidencia = models.TextField(db_column='Tipo_Incidencia')  # Field name made lowercase.
    segmento = models.TextField(db_column='Segmento')  # Field name made lowercase.
    n2_categ_prod = models.TextField(db_column='N2_Categ_Prod')  # Field name made lowercase.
    n3_categ_prod = models.TextField(db_column='N3_Categ_Prod')  # Field name made lowercase.
    n1_cat_ope = models.TextField(db_column='N1_Cat_Ope')  # Field name made lowercase.
    n2_cat_ope = models.TextField(db_column='N2_Cat_Ope')  # Field name made lowercase. 
    n3_cat_ope = models.TextField(db_column='N3_Cat_Ope')  # Field name made lowercase.
    urgencia = models.TextField(db_column='Urgencia')  # Field name made lowercase.
    prioridad = models.TextField(db_column='Prioridad')  # Field name made lowercase. 
    fecha_cierre = models.TextField(db_column='Fecha_Cierre')  # Field name made lowercase.
    assigned_company = models.TextField(db_column='Assigned_Company')  # Field name made lowercase.
    assigned_org = models.TextField(db_column='Assigned_Org')  # Field name made lowercase.
    usuario_asignado = models.TextField(db_column='Usuario_Asignado')  # Field name made lowercase.
    remitente = models.TextField(db_column='Remitente')  # Field name made lowercase.
    ultima_mod = models.TextField(db_column='Ultima_Mod')  # Field name made lowercase.
    celula_n = models.IntegerField(db_column='Celula_N')  # Field name made lowercase.        

    class Meta:
        managed = True
        db_table = 'CSV_Importado6'

class CsvImportado7(models.Model):
    id = models.TextField(db_column='ID',primary_key=True)  # Field name made lowercase.
    grupo_asignado = models.TextField(db_column='Grupo_Asignado')  # Field name made lowercase. 
    estado = models.TextField(db_column='Estado')  # Field name made lowercase.
    status_reason_hidden = models.TextField(db_column='Status_Reason_Hidden')  # Field name made lowercase.
    id_cliente = models.TextField(db_column='ID_Cliente')  # Field name made lowercase.
    razon_social = models.TextField(db_column='Razon_Social')  # Field name made lowercase.
    cliente_sidi = models.TextField(db_column='Cliente_SIDI')  # Field name made lowercase.
    ci = models.TextField(db_column='CI')  # Field name made lowercase.
    clase_ci = models.TextField(db_column='CLASE_CI')  # Field name made lowercase.
    fecha_envio = models.TextField(db_column='Fecha_Envio')  # Field name made lowercase.
    tipo_incidencia = models.TextField(db_column='Tipo_Incidencia')  # Field name made lowercase.
    segmento = models.TextField(db_column='Segmento')  # Field name made lowercase.
    n2_categ_prod = models.TextField(db_column='N2_Categ_Prod')  # Field name made lowercase.
    n3_categ_prod = models.TextField(db_column='N3_Categ_Prod')  # Field name made lowercase.
    n1_cat_ope = models.TextField(db_column='N1_Cat_Ope')  # Field name made lowercase.
    n2_cat_ope = models.TextField(db_column='N2_Cat_Ope')  # Field name made lowercase. 
    n3_cat_ope = models.TextField(db_column='N3_Cat_Ope')  # Field name made lowercase.
    urgencia = models.TextField(db_column='Urgencia')  # Field name made lowercase.
    prioridad = models.TextField(db_column='Prioridad')  # Field name made lowercase. 
    fecha_cierre = models.TextField(db_column='Fecha_Cierre')  # Field name made lowercase.
    assigned_company = models.TextField(db_column='Assigned_Company')  # Field name made lowercase.
    assigned_org = models.TextField(db_column='Assigned_Org')  # Field name made lowercase.
    usuario_asignado = models.TextField(db_column='Usuario_Asignado')  # Field name made lowercase.
    remitente = models.TextField(db_column='Remitente')  # Field name made lowercase.
    ultima_mod = models.TextField(db_column='Ultima_Mod')  # Field name made lowercase.
    celula_n = models.IntegerField(db_column='Celula_N')  # Field name made lowercase.        

    class Meta:
        managed = True
        db_table = 'CSV_Importado7'

class CsvImportado8(models.Model):
    id = models.TextField(db_column='ID',primary_key=True)  # Field name made lowercase.
    grupo_asignado = models.TextField(db_column='Grupo_Asignado')  # Field name made lowercase. 
    estado = models.TextField(db_column='Estado')  # Field name made lowercase.
    status_reason_hidden = models.TextField(db_column='Status_Reason_Hidden')  # Field name made lowercase.
    id_cliente = models.TextField(db_column='ID_Cliente')  # Field name made lowercase.
    razon_social = models.TextField(db_column='Razon_Social')  # Field name made lowercase.
    cliente_sidi = models.TextField(db_column='Cliente_SIDI')  # Field name made lowercase.
    ci = models.TextField(db_column='CI')  # Field name made lowercase.
    clase_ci = models.TextField(db_column='CLASE_CI')  # Field name made lowercase.
    fecha_envio = models.TextField(db_column='Fecha_Envio')  # Field name made lowercase.
    tipo_incidencia = models.TextField(db_column='Tipo_Incidencia')  # Field name made lowercase.
    segmento = models.TextField(db_column='Segmento')  # Field name made lowercase.
    n2_categ_prod = models.TextField(db_column='N2_Categ_Prod')  # Field name made lowercase.
    n3_categ_prod = models.TextField(db_column='N3_Categ_Prod')  # Field name made lowercase.
    n1_cat_ope = models.TextField(db_column='N1_Cat_Ope')  # Field name made lowercase.
    n2_cat_ope = models.TextField(db_column='N2_Cat_Ope')  # Field name made lowercase. 
    n3_cat_ope = models.TextField(db_column='N3_Cat_Ope')  # Field name made lowercase.
    urgencia = models.TextField(db_column='Urgencia')  # Field name made lowercase.
    prioridad = models.TextField(db_column='Prioridad')  # Field name made lowercase. 
    fecha_cierre = models.TextField(db_column='Fecha_Cierre')  # Field name made lowercase.
    assigned_company = models.TextField(db_column='Assigned_Company')  # Field name made lowercase.
    assigned_org = models.TextField(db_column='Assigned_Org')  # Field name made lowercase.
    usuario_asignado = models.TextField(db_column='Usuario_Asignado')  # Field name made lowercase.
    remitente = models.TextField(db_column='Remitente')  # Field name made lowercase.
    ultima_mod = models.TextField(db_column='Ultima_Mod')  # Field name made lowercase.
    celula_n = models.IntegerField(db_column='Celula_N')  # Field name made lowercase.        

    class Meta:
        managed = True
        db_table = 'CSV_Importado8'

class CsvImportado9(models.Model):
    id = models.TextField(db_column='ID',primary_key=True)  # Field name made lowercase.
    grupo_asignado = models.TextField(db_column='Grupo_Asignado')  # Field name made lowercase. 
    estado = models.TextField(db_column='Estado')  # Field name made lowercase.
    status_reason_hidden = models.TextField(db_column='Status_Reason_Hidden')  # Field name made lowercase.
    id_cliente = models.TextField(db_column='ID_Cliente')  # Field name made lowercase.
    razon_social = models.TextField(db_column='Razon_Social')  # Field name made lowercase.
    cliente_sidi = models.TextField(db_column='Cliente_SIDI')  # Field name made lowercase.
    ci = models.TextField(db_column='CI')  # Field name made lowercase.
    clase_ci = models.TextField(db_column='CLASE_CI')  # Field name made lowercase.
    fecha_envio = models.TextField(db_column='Fecha_Envio')  # Field name made lowercase.
    tipo_incidencia = models.TextField(db_column='Tipo_Incidencia')  # Field name made lowercase.
    segmento = models.TextField(db_column='Segmento')  # Field name made lowercase.
    n2_categ_prod = models.TextField(db_column='N2_Categ_Prod')  # Field name made lowercase.
    n3_categ_prod = models.TextField(db_column='N3_Categ_Prod')  # Field name made lowercase.
    n1_cat_ope = models.TextField(db_column='N1_Cat_Ope')  # Field name made lowercase.
    n2_cat_ope = models.TextField(db_column='N2_Cat_Ope')  # Field name made lowercase. 
    n3_cat_ope = models.TextField(db_column='N3_Cat_Ope')  # Field name made lowercase.
    urgencia = models.TextField(db_column='Urgencia')  # Field name made lowercase.
    prioridad = models.TextField(db_column='Prioridad')  # Field name made lowercase. 
    fecha_cierre = models.TextField(db_column='Fecha_Cierre')  # Field name made lowercase.
    assigned_company = models.TextField(db_column='Assigned_Company')  # Field name made lowercase.
    assigned_org = models.TextField(db_column='Assigned_Org')  # Field name made lowercase.
    usuario_asignado = models.TextField(db_column='Usuario_Asignado')  # Field name made lowercase.
    remitente = models.TextField(db_column='Remitente')  # Field name made lowercase.
    ultima_mod = models.TextField(db_column='Ultima_Mod')  # Field name made lowercase.
    celula_n = models.IntegerField(db_column='Celula_N')  # Field name made lowercase.        

    class Meta:
        managed = True
        db_table = 'CSV_Importado9'

class CsvImportado10(models.Model):
    id = models.TextField(db_column='ID',primary_key=True)  # Field name made lowercase.
    grupo_asignado = models.TextField(db_column='Grupo_Asignado')  # Field name made lowercase. 
    estado = models.TextField(db_column='Estado')  # Field name made lowercase.
    status_reason_hidden = models.TextField(db_column='Status_Reason_Hidden')  # Field name made lowercase.
    id_cliente = models.TextField(db_column='ID_Cliente')  # Field name made lowercase.
    razon_social = models.TextField(db_column='Razon_Social')  # Field name made lowercase.
    cliente_sidi = models.TextField(db_column='Cliente_SIDI')  # Field name made lowercase.
    ci = models.TextField(db_column='CI')  # Field name made lowercase.
    clase_ci = models.TextField(db_column='CLASE_CI')  # Field name made lowercase.
    fecha_envio = models.TextField(db_column='Fecha_Envio')  # Field name made lowercase.
    tipo_incidencia = models.TextField(db_column='Tipo_Incidencia')  # Field name made lowercase.
    segmento = models.TextField(db_column='Segmento')  # Field name made lowercase.
    n2_categ_prod = models.TextField(db_column='N2_Categ_Prod')  # Field name made lowercase.
    n3_categ_prod = models.TextField(db_column='N3_Categ_Prod')  # Field name made lowercase.
    n1_cat_ope = models.TextField(db_column='N1_Cat_Ope')  # Field name made lowercase.
    n2_cat_ope = models.TextField(db_column='N2_Cat_Ope')  # Field name made lowercase. 
    n3_cat_ope = models.TextField(db_column='N3_Cat_Ope')  # Field name made lowercase.
    urgencia = models.TextField(db_column='Urgencia')  # Field name made lowercase.
    prioridad = models.TextField(db_column='Prioridad')  # Field name made lowercase. 
    fecha_cierre = models.TextField(db_column='Fecha_Cierre')  # Field name made lowercase.
    assigned_company = models.TextField(db_column='Assigned_Company')  # Field name made lowercase.
    assigned_org = models.TextField(db_column='Assigned_Org')  # Field name made lowercase.
    usuario_asignado = models.TextField(db_column='Usuario_Asignado')  # Field name made lowercase.
    remitente = models.TextField(db_column='Remitente')  # Field name made lowercase.
    ultima_mod = models.TextField(db_column='Ultima_Mod')  # Field name made lowercase.
    celula_n = models.IntegerField(db_column='Celula_N')  # Field name made lowercase.        

    class Meta:
        managed = True
        db_table = 'CSV_Importado10'


class Tablaseguimiento(models.Model):
    ATENCION = (('0','URGENTE'),('1','PRIORITARIO'),('2','NORMAL'))
    
    orderid = models.AutoField(db_column='OrderId',primary_key=True)  # Field name made lowercase.
    detalle = models.CharField(max_length=200, blank=True, null=True, default='')
    reactivar = models.DateField(blank=True, null=True, default=None)
    reactivar_hora = models.TimeField(blank=True,null=True)
    prioridad = models.CharField(max_length=100, blank=True, null=True, choices = ATENCION, default = '2')
    tkt = models.OneToOneField(CsvImportado1,on_delete = models.CASCADE, related_name='tkt')

    class Meta:                                                                     
        managed = True
        db_table = 'TablaSeguimiento'

    def __str__(self):
        return str(self.orderid)


class Eventostkt(models.Model):
    sk = models.AutoField(db_column='SK', primary_key=True)  # Field name made lowercase.
    id = models.CharField(db_column='ID', max_length=250, blank=True, null=True)  # Field name made lowercase.
    grupo_asignado = models.CharField(db_column='Grupo_Asignado', max_length=250, blank=True, null=True)  # Field name made lowercase.
    grupo_asignado_anterior = models.CharField(db_column='Grupo_Asignado_anterior', max_length=250, blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=250, blank=True, null=True)  # Field name made lowercase.
    estado_anterior = models.CharField(db_column='Estado_anterior', max_length=250, blank=True, null=True)  # Field name made lowercase.
    status_reason_hidden = models.CharField(db_column='Status_Reason_Hidden', max_length=250, blank=True, null=True)  # Field name made lowercase.
    status_reason_hidden_anterior = models.CharField(db_column='Status_Reason_Hidden_anterior', max_length=250, blank=True, null=True)  # Field name made lowercase.
    tipo_incidencia = models.CharField(db_column='Tipo_Incidencia', max_length=250, blank=True, null=True)  # Field name made lowercase.                   
    tipo_incidencia_anterior = models.CharField(db_column='Tipo_Incidencia_anterior', max_length=250, blank=True, null=True)  # Field name made lowercase.
    fecha_envio = models.CharField(db_column='Fecha_Envio', max_length=250, blank=True, null=True)  # Field name made lowercase.                                                  
    tiempo_acumulado = models.CharField(db_column='Tiempo_Acumulado', max_length=250, blank=True, null=True)  # Field name made lowercase.
    horario = models.DateTimeField(db_column='Horario')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'eventostkt'                                                                                                                         


#se actaiva depues de un guardado.
#post_save.connect(prueba_signals, sender = Tablaseguimiento)

#post_delete.connect(prueba_signals2, sender = Tablaseguimiento)