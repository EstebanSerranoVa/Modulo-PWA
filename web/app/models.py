# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Acompanante(models.Model):
    id_acompanante = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=255)
    id_reserva = models.ForeignKey('Reserva', models.DO_NOTHING, db_column='id_reserva')

    class Meta:
        managed = False
        db_table = 'acompanante'

    def __str__(self):
        return self.nombre


class Admin(models.Model):
    id_admin = models.AutoField(primary_key=True)
    id_cuenta = models.ForeignKey('Cuenta', models.DO_NOTHING, db_column='id_cuenta')
    activo = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'admin'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.AutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CheckIn(models.Model):
    id_cechkin = models.AutoField(primary_key=True)
    fecha = models.DateField()
    hora = models.DateTimeField()
    pago_pendiente = models.BigIntegerField()
    id_reserva = models.ForeignKey('Reserva', models.DO_NOTHING, db_column='id_reserva')

    class Meta:
        managed = False
        db_table = 'check_in'
    def __str__(self):
        return self.fecha

class CheckOut(models.Model):
    id_checkout = models.AutoField(primary_key=True)
    fecha = models.DateField()
    hora = models.DateTimeField()
    multa = models.BigIntegerField(blank=True, null=True)
    id_reserva = models.ForeignKey('Reserva', models.DO_NOTHING, db_column='id_reserva')
    detalle = models.CharField(max_length=255, blank=True, null=True)
    costo_reparacion = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'check_out'
    def __str__(self):
        return self.fecha


class Cliente(models.Model):
    id_cliente = models.BigIntegerField(primary_key=True, verbose_name="Identificador Cliente")
    id_cuenta = models.ForeignKey('Cuenta', models.DO_NOTHING, db_column='id_cuenta', verbose_name="Cuenta")
    activo = models.CharField(max_length=1, verbose_name="¿Esta Activo?")

    class Meta:
        managed = False
        db_table = 'cliente'
    def __str__(self):
        return self.id_cuenta


class Comuna(models.Model):
    id_co = models.BigIntegerField(primary_key=True)
    id_pr = models.ForeignKey('Provincia', models.DO_NOTHING, db_column='id_pr')
    str_descripcion = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comuna'
    def __str__(self):
        return self.str_descripcion


class Conductor(models.Model):
    id_conductor = models.BigIntegerField(primary_key=True)
    rut = models.CharField(max_length=15)
    nombre = models.CharField(max_length=15)
    apellidop = models.CharField(max_length=15, verbose_name="Apellido Paterno")
    activo = models.CharField(max_length=1, blank=True, null=True, verbose_name="¿Esta Activo?")

    class Meta:
        managed = False
        db_table = 'conductor'
    
    def __str__(self):
        return self.nombre


class Cuenta(models.Model):
    id_cuenta = models.BigIntegerField(primary_key=True)
    correo = models.CharField(unique=True, max_length=100)
    rut = models.CharField(max_length=15)
    nombre = models.CharField(max_length=20)
    apellidop = models.CharField(max_length=20)
    apellidom = models.CharField(max_length=20)
    telefono = models.BigIntegerField(blank=True, null=True)
    celular = models.BigIntegerField()
    id_tipocuenta = models.ForeignKey('TipoCuenta', models.DO_NOTHING, db_column='id_tipocuenta')
    contrasena = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'cuenta'
    
    def __str__(self):
        return self.nombre


opciones = [
    (0, "No"),
    (1, "Si")
]


 
class Departamento(models.Model):
    id_departamento = models.BigIntegerField(primary_key=True, verbose_name="Identificador Departamento") 
    numero = models.BigIntegerField()
    piso = models.BigIntegerField()
    tarifa = models.BigIntegerField()
    porcentaje_reserva = models.BigIntegerField()
    descripcion = models.CharField(max_length=200)
    activo = models.IntegerField(verbose_name="¿Esta Activo?")
    id_estado = models.ForeignKey('Estado', models.DO_NOTHING, db_column='id_estado', verbose_name="Estado Departamento")
    id_edificio = models.ForeignKey('Edificio', models.DO_NOTHING, db_column='id_edificio', blank=True, null=True, verbose_name="Edificio")
    foto = models.ImageField(upload_to="departamentos")

    class Meta:
        managed = False
        db_table = 'departamento'
    
    def __str__(self):
        return self.descripcion


class Direccion(models.Model):
    id_direccion = models.BigIntegerField(primary_key=True)
    calle = models.CharField(max_length=30)
    numero = models.BigIntegerField()
    id_co = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='id_co')

    class Meta:
        managed = False
        db_table = 'direccion'
    def __str__(self):
        return self.calle
  
    


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.AutoField(primary_key=True)
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Edificio(models.Model):
    id_edificio = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    activo = models.CharField(max_length=1)
    id_direccion = models.ForeignKey(Direccion, models.DO_NOTHING, db_column='id_direccion')

    class Meta:
        managed = False
        db_table = 'edificio'
    
    def __str__(self):
        return self.nombre


class Estado(models.Model):
    id_estado = models.BigIntegerField(primary_key=True)
    descripcion = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'estado'
    def __str__(self):
        return self.descripcion
    


class Funcionario(models.Model):
    id_funcionario = models.BigIntegerField(primary_key=True)
    id_cuenta = models.ForeignKey(Cuenta, models.DO_NOTHING, db_column='id_cuenta')
    activo = models.CharField(max_length=1)
    id_edificio = models.ForeignKey(Edificio, models.DO_NOTHING, db_column='id_edificio')

    class Meta:
        managed = False
        db_table = 'funcionario'
    def __str__(self):
        return self.id_funcionario


class Item(models.Model):
    id_item = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    costo = models.BigIntegerField()
    activo = models.CharField(max_length=1)
    id_departamento = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='id_departamento')

    class Meta:
        managed = False
        db_table = 'item'
    
    def __str__(self):
        return self.nombre


class Mantencion(models.Model):
    id_mantencion = models.BigIntegerField(primary_key=True)
    fecha = models.DateField()
    id_tipomantencion = models.ForeignKey('TipoMantencion', models.DO_NOTHING, db_column='id_tipomantencion', verbose_name='Tipo Mantención')
    id_departamento = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='id_departamento', verbose_name="Identificador Edificio")
    costo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mantencion'

    def __str__(self):
        return self.id_departamento



class Provincia(models.Model):
    id_pr = models.BigIntegerField(primary_key=True)
    id_re = models.ForeignKey('Region', models.DO_NOTHING, db_column='id_re')
    str_descripcion = models.CharField(max_length=30, blank=True, null=True)
    num_comunas = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'provincia'
    def __str__(self):
        return self.str_descripcion


class Region(models.Model):
    id_re = models.BigIntegerField(primary_key=True)
    str_descripcion = models.CharField(max_length=60)
    str_roman = models.CharField(max_length=5)
    num_provincias = models.BigIntegerField()
    num_comunas = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'region'
    def __str__(self):
        return self.str_descripcion

class Reserva(models.Model):
    id_reserva = models.BigIntegerField(primary_key=True)
    fecha_ingreso = models.DateField()
    fecha_salida = models.DateField()
    pago_reserva = models.BigIntegerField()
    total_pagar = models.BigIntegerField()
    id_reservaestado = models.ForeignKey('ReservaEstado', models.DO_NOTHING, db_column='id_reservaestado', blank=True, null=True)
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente')
    id_transporte = models.ForeignKey('Transporte', models.DO_NOTHING, db_column='id_transporte', blank=True, null=True)
    id_departamento = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='id_departamento')

    class Meta:
        managed = False
        db_table = 'reserva'
    
    def __str__(self):
        return self.id_reserva


class ReservaEstado(models.Model):
    id_reservaestado = models.BigIntegerField(primary_key=True)
    descripcion = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'reserva_estado'
    def __str__(self):
        return self.id_reservaestado


class ReservaTour(models.Model):
    id_reservatour = models.BigIntegerField(primary_key=True)
    id_reserva = models.ForeignKey(Reserva, models.DO_NOTHING, db_column='id_reserva')
    id_tour = models.ForeignKey('Tour', models.DO_NOTHING, db_column='id_tour')

    class Meta:
        managed = False
        db_table = 'reserva_tour'
    def __str__(self):
        return self.id_reservatour


class TipoCuenta(models.Model):
    id_tipocuenta = models.BigIntegerField(primary_key=True)
    descripcion = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'tipo_cuenta'
    def __str__(self):
        return self.descripcion


class TipoMantencion(models.Model):
    id_tipomantencion = models.BigIntegerField(primary_key=True)
    descripcion = models.CharField(max_length=50)
    costo = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'tipo_mantencion'
    def __str__(self):
        return self.descripcion


class Tour(models.Model):
    id_tour = models.BigIntegerField(primary_key=True, verbose_name="Identificador Tour")
    lugar = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200, verbose_name="Descripción")
    fecha = models.DateField()
    hora_comienzo = models.TimeField()
    hora_fin = models.TimeField()
    precio = models.BigIntegerField()
    capacidad = models.BigIntegerField()
    activo = models.CharField(max_length=1, verbose_name="¿Esta Activo?")
    foto = models.ImageField(blank=True, null=True)
    id_direccion = models.ForeignKey(Direccion, models.DO_NOTHING, db_column='id_direccion', verbose_name="Dirección")


    
    class Meta:
        managed = False
        db_table = 'tour'
    
    def __str__(self):
        return self.lugar


class Transporte(models.Model):
    id_transporte = models.BigIntegerField(primary_key=True)
    id_vehiculo = models.ForeignKey('Vehiculo', models.DO_NOTHING, db_column='id_vehiculo', blank=True, null=True)
    id_conductor = models.ForeignKey(Conductor, models.DO_NOTHING, db_column='id_conductor', blank=True, null=True)
    activo = models.CharField(max_length=1, blank=True, null=True)
    precio = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transporte'
    
  



class Vehiculo(models.Model):
    id_vehiculo = models.BigIntegerField(primary_key=True)
    patente = models.CharField(max_length=10)
    marca = models.CharField(max_length=15)
    modelo = models.CharField(max_length=15)
    anio = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'vehiculo'
    
    def __str__(self):
        return self.id_vehiculo
