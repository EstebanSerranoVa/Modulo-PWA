from django.contrib import admin
from .models import Departamento, Item, Mantencion, Reserva, Acompanante, CheckIn, CheckOut, Cliente, Comuna, Conductor, Direccion, Edificio, Estado,Funcionario, \
    Item, Provincia, Region, TipoCuenta, TipoMantencion, Tour, Transporte, Vehiculo



class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ["id_departamento" ,"piso", "numero", "tarifa", "porcentaje_reserva", "descripcion", "activo", "id_estado", "id_edificio"]
    list_editable = ["tarifa", "porcentaje_reserva"]
    list_per_page = 10
    
class MantencionAdmin(admin.ModelAdmin):
    list_display = ["id_mantencion" ,"fecha", "id_tipomantencion", "id_departamento", "costo"]
    list_editable = ["costo"]
    list_per_page = 10
    

# Register your models here.

admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Reserva)
admin.site.register(Acompanante)
admin.site.register(CheckIn)
admin.site.register(CheckOut)
admin.site.register(Cliente)
admin.site.register(Comuna)
admin.site.register(Conductor)
admin.site.register(Direccion)
admin.site.register(Edificio)
admin.site.register(Estado)
admin.site.register(Funcionario)
admin.site.register(Item)
admin.site.register(Provincia)
admin.site.register(Region)
admin.site.register(TipoCuenta)
admin.site.register(TipoMantencion)
admin.site.register(Tour)
admin.site.register(Transporte)
admin.site.register(Vehiculo)










