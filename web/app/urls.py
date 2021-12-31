from django.urls import path, include
from .views import eliminarMant, home, contacto, galeria, agregarDpto, listarDpto, modificarDpto, eliminarDpto, DepartamentoViewset, \
    agregarCli, listarCli, modificarCli, eliminarCli, agregarMant,listarMant, modificarMant, \
    modificarMant, eliminarMant, agregarTour, listarTour, modificarTour, eliminarTour, agregarConductor, listarConductor, modificarConductor, eliminarConductor, \
      agregarVehiculo, listarVehiculo, modificarVehiculo, eliminarVehiculo, \
        agregarFuncionario, listarFuncionario, eliminarFuncionario, modificarFuncionario
from rest_framework import routers

## API ##########
router = routers.DefaultRouter()
router.register('dpto', DepartamentoViewset)


urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('galeria/', galeria, name="galeria"),
    path('agregarDpto/', agregarDpto, name="agregarDpto"),
    path('listarDpto/', listarDpto, name="listarDpto"),
    path('modificarDpto/<id_departamento>/', modificarDpto, name="modificarDpto"),
    path('eliminarDpto/<id_departamento>/', eliminarDpto, name="eliminarDpto"),
    path('api/', include(router.urls)),
    ################# CLiente #####################
    path('agregarCli/', agregarCli, name="agregarCli"),
    path('listarCli/', listarCli, name="listarCli"),
    path('modificarCli/<id_cliente>/', modificarCli, name="modificarCli"),
    path('eliminarCli/<id_cliente>/', eliminarCli, name="eliminarCli"),
    ############### Mantención ###########################

    path('agregarMant/', agregarMant, name="agregarMant"),
    path('listarMant/', listarMant, name="listarMant"),
    path('modificarMant/<id_mantencion>/', modificarMant, name="modificarMant"),
    path('eliminarMant/<id_mantencion>/', eliminarMant, name="eliminarMant"),

      ############### Tour ###########################

    path('agregarTour/', agregarTour, name="agregarTour"),
    path('listarTour/', listarTour, name="listarTour"),
    path('modificarTour/<id_tour>/', modificarTour, name="modificarTour"),
    path('eliminarTour/<id_tour>/', eliminarTour, name="eliminarTour"),


     ############### Conductor ###########################

    path('agregarConductor/', agregarConductor, name="agregarConductor"),
    path('listarConductor/', listarConductor, name="listarConductor"),
    path('modificarConductor/<id_conductor>/', modificarConductor, name="modificarConductor"),
    path('eliminarConductor/<id_conductor>/', eliminarConductor, name="eliminarConductor"),

    ############### Auto ###########################

    path('agregarVehiculo/', agregarVehiculo, name="agregarVehiculo"),
    path('listarVehiculo/', listarVehiculo, name="listarVehiculo"),
    path('modificarVehiculo/<id_vehiculo>/', modificarVehiculo, name="modificarVehiculo"),
    path('eliminarVehiculo/<id_vehiculo>/', eliminarVehiculo, name="eliminarVehiculo"),


    ############### Funcionario ###########################

    path('agregarFuncionario/', agregarFuncionario, name="agregarFuncionario"),
    path('listarFuncionario/', listarFuncionario, name="listarFuncionario"),
    path('modificarFuncionario/<id_funcionario>/', modificarFuncionario, name="modificarFuncionario"),
    path('eliminarFuncionario/<id_funcionario>/', eliminarFuncionario, name="eliminarFuncionario"),

]
