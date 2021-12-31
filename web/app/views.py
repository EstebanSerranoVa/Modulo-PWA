from django.core import paginator
from django.http import request
from django.http.response import Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Conductor, Departamento, Funcionario, Mantencion, Tour, Vehiculo
from .forms import DepartamentoForm, ClienteForm, FuncionarioForm, MantencionForm, TourForm, ConductorForm, VehiculoForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework import serializers, viewsets
from .serializers import DepartamentoSerializer
# Create your views here.

class DepartamentoViewset(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializers_class = DepartamentoSerializer






def home(reques):
    departamentos = Departamento.objects.all()
    data = {
        'departamentos': departamentos
    }
    return render(reques, 'app/home.html', data)

def contacto(reques):
    return render(reques, 'app/contacto.html')

def galeria(reques):
    return render(reques, 'app/galeria.html')

############ DEPARTAMENTOS ################
@permission_required('app.add_departamento')
def agregarDpto(reques):

    data = {
        'form': DepartamentoForm()
    }

    if reques.method == 'POST':
        formulario = DepartamentoForm(data=reques.POST, files=reques.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(reques, "Agregado Correctamente")
        else:
            data["form"] = formulario

    return render(reques, 'app/departamento/agregarDpto.html', data)


def listarDpto(reques):
    departamentos = Departamento.objects.all()
    page = reques.GET.get('page', 1)

    try:
        paginator = Paginator(departamentos, 5)
        departamentos = paginator.page(page)
    except:
        raise Http404



    data = {
        'entity': departamentos,
        'paginator': paginator

    }

    return render(reques, 'app/departamento/listarDpto.html', data)


def modificarDpto(request, id_departamento):

    departamento = get_object_or_404(Departamento, id_departamento=id_departamento)

    data = {
        'form': DepartamentoForm(instance=departamento)
    }

    if request.method == "POST":
        formulario = DepartamentoForm(data=request.POST, instance=departamento, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to="listarDpto")
        data["form"] = formulario

    return render(request, 'app/departamento/modificarDpto.html', data)


def eliminarDpto(request, id_departamento):
    departamento = get_object_or_404(Departamento, id_departamento=id_departamento)
    departamento.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="listarDpto")



########### ClIENTES #######################
def agregarCli(reques):

    data = {
        'form': ClienteForm()
    }

    if reques.method == 'POST':
        formulario = ClienteForm(data=reques.POST, files=reques.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Agregado Correctamente")
        else:
            data["form"] = formulario

    return render(reques, 'app/cliente/agregarCli.html', data)


def listarCli(reques):
    clientes = Cliente.objects.all()
    page = reques.GET.get('page', 1)

    try:
        paginator = Paginator(clientes, 5)
        clientes = paginator.page(page)
    except:
        raise Http404



    data = {
        'entity': clientes,
        'paginator': paginator

    }

    return render(reques, 'app/cliente/listarCli.html', data)


def modificarCli(request, id_cliente):

    clientes = get_object_or_404(Cliente, id_cliente=id_cliente)

    data = {
        'form': ClienteForm(instance=clientes)
    }

    if request.method == "POST":
        formulario = ClienteForm(data=request.POST, instance=clientes, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to="listarCli")
        data["form"] = formulario

    return render(request, 'app/cliente/modificarCli.html', data)


def eliminarCli(request, id_cliente):
    clientes = get_object_or_404(Cliente, id_cliente=id_cliente)
    clientes.delete()
    return redirect(to="listarCli")




############## MAntencion ###############################
def agregarMant(reques):

    data = {
        'form': MantencionForm()
    }

    if reques.method == 'POST':
        formulario = MantencionForm(data=reques.POST, files=reques.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(reques, "Agregado Correctamente")
        else:
            data["form"] = formulario

    return render(reques, 'app/mantencion/agregarMant.html', data)


def listarMant(reques):
    mantencione = Mantencion.objects.all()
    page = reques.GET.get('page', 1)

    try:
        paginator = Paginator(mantencione, 5)
        mantencione = paginator.page(page)
    except:
        raise Http404



    data = {
        'entity': mantencione,
        'paginator': paginator

    }

    return render(reques, 'app/mantencion/listarMant.html', data)


def modificarMant(request, id_mantencion):

    mantencion = get_object_or_404(Mantencion, id_mantencion=id_mantencion)

    data = {
        'form': MantencionForm(instance=mantencion)
    }

    if request.method == "POST":
        formulario = MantencionForm(data=request.POST, instance=mantencion, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to="listarMant")
        data["form"] = formulario

    return render(request, 'app/mantencion/modificarMant.html', data)


def eliminarMant(reques, id_mantencion):
    mantencione = get_object_or_404(Mantencion, id_mantencion=id_mantencion)
    mantencione.delete()
    return redirect(to="listarMant")




############## Tour ###############################
def agregarTour(reques):

    data = {
        'form': TourForm()
    }

    if reques.method == 'POST':
        formulario = TourForm(data=reques.POST, files=reques.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(reques, "Agregado Correctamente")
        else:
            data["form"] = formulario

    return render(reques, 'app/tour/agregarTour.html', data)


def listarTour(reques):
    tour = Tour.objects.all()
    page = reques.GET.get('page', 1)

    try:
        paginator = Paginator(tour, 5)
        tour = paginator.page(page)
    except:
        raise Http404



    data = {
        'entity': tour,
        'paginator': paginator

    }

    return render(reques, 'app/tour/listarTour.html', data)


def modificarTour(request, id_tour):

    tour = get_object_or_404(Tour, id_tour=id_tour)

    data = {
        'form': TourForm(instance=tour)
    }

    if request.method == "POST":
        formulario = TourForm(data=request.POST, instance=tour, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to="listarTour")
        data["form"] = formulario

    return render(request, 'app/tour/modificarTour.html', data)


def eliminarTour(reques, id_tour): 
    tour = get_object_or_404(Tour, id_tour=id_tour)
    tour.delete()
    return redirect(to="listarTour")



############## Conductor ###############################
def agregarConductor(reques):

    data = {
        'form': ConductorForm()
    }

    if reques.method == 'POST':
        formulario = ConductorForm(data=reques.POST, files=reques.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(reques, "Agregado Correctamente")
        else:
            data["form"] = formulario

    return render(reques, 'app/conductor/agregarConductor.html', data)


def listarConductor(reques):
    conductor = Conductor.objects.all()
    page = reques.GET.get('page', 1)

    try:
        paginator = Paginator(conductor, 5)
        conductor = paginator.page(page)
    except:
        raise Http404



    data = {
        'entity': conductor,
        'paginator': paginator

    }

    return render(reques, 'app/conductor/listarConductor.html', data)


def modificarConductor(request, id_conductor):

    conductor = get_object_or_404(Conductor, id_conductor=id_conductor)

    data = {
        'form': ConductorForm(instance=conductor)
    }

    if request.method == "POST":
        formulario = ConductorForm(data=request.POST, instance=conductor, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to="listarConductor")
        data["form"] = formulario

    return render(request, 'app/conductor/modificarConductor.html', data)


def eliminarConductor(reques, id_conductor):
    conductor = get_object_or_404(Conductor, id_conductor=id_conductor)
    conductor.delete()
    return redirect(to="listarConductor")






############## Vehiculo ###############################
def agregarVehiculo(reques):

    data = {
        'form': VehiculoForm()
    }

    if reques.method == 'POST':
        formulario = VehiculoForm(data=reques.POST, files=reques.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(reques, "Agregado Correctamente")
        else:
            data["form"] = formulario

    return render(reques, 'app/auto/agregarAuto.html', data)


def listarVehiculo(reques):
    vehiculo = Vehiculo.objects.all()
    page = reques.GET.get('page', 1)

    try:
        paginator = Paginator(vehiculo, 5)
        vehiculo = paginator.page(page)
    except:
        raise Http404



    data = {
        'entity': vehiculo,
        'paginator': paginator

    }

    return render(reques, 'app/auto/listarAuto.html', data)


def modificarVehiculo(request, id_vehiculo):

    vehiculo = get_object_or_404(Vehiculo, id_vehiculo=id_vehiculo)

    data = {
        'form': VehiculoForm(instance=vehiculo)
    }

    if request.method == "POST":
        formulario = VehiculoForm(data=request.POST, instance=vehiculo, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to="listarVehiculo")
        data["form"] = formulario

    return render(request, 'app/auto/modificarAuto.html', data)


def eliminarVehiculo(reques, id_vehiculo):
    vehiculo = get_object_or_404(Vehiculo, id_vehiculo=id_vehiculo)
    vehiculo.delete()
    return redirect(to="listarVehiculo")






############## Funcioanrio ###############################
def agregarFuncionario(reques):

    data = {
        'form': FuncionarioForm()
    }

    if reques.method == 'POST':
        formulario = FuncionarioForm(data=reques.POST, files=reques.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(reques, "Agregado Correctamente")
        else:
            data["form"] = formulario

    return render(reques, 'app/funcionario/agregarFuncionario.html', data)


def listarFuncionario(reques):
    funcionario = Funcionario.objects.all()
    page = reques.GET.get('page', 1)

    try:
        paginator = Paginator(funcionario, 5)
        funcionario = paginator.page(page)
    except:
        raise Http404



    data = {
        'entity': funcionario,
        'paginator': paginator

    }

    return render(reques, 'app/funcionario/listarFuncionario.html', data)


def modificarFuncionario(request, id_funcionario):

    funcionario = get_object_or_404(Funcionario, id_funcionario=id_funcionario)

    data = {
        'form': FuncionarioForm(instance=funcionario)
    }

    if request.method == "POST":
        formulario = FuncionarioForm(data=request.POST, instance=funcionario, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to="listarFuncionario")
        data["form"] = formulario

    return render(request, 'app/funcionario/modificarFuncionario.html', data)


def eliminarFuncionario(reques, id_funcionario):
    funcionario = get_object_or_404(Funcionario, id_funcionario=id_funcionario)
    funcionario.delete()
    return redirect(to="listarFuncionario")