from django import forms
from django.forms import widgets
from .models import Departamento, Cliente, Mantencion, Tour, Conductor, Transporte, Vehiculo, Funcionario




class DepartamentoForm(forms.ModelForm):
    activo = forms.IntegerField(min_value=0, max_value=1)
    

    class Meta:
        model = Departamento
        fields = ["id_departamento", "numero","piso","tarifa","porcentaje_reserva","descripcion","activo","id_estado","id_edificio"]
       
        widgets ={
        
        'porcentaje_reserva': forms.TextInput(attrs={'placeholder': 'no Ingresar %'}),
        
        }

  
class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = "__all__"
        

class MantencionForm(forms.ModelForm):

    class Meta:
        model = Mantencion
        fields = "__all__"
      
        widgets ={
        "fecha": forms.SelectDateWidget()
        }
   

class TourForm(forms.ModelForm):

    class Meta:
        model = Tour
        fields = ["id_tour","lugar","descripcion","fecha","hora_comienzo","hora_fin","precio","capacidad","activo","id_direccion"]

        widgets = {
            "fecha": forms.SelectDateWidget()
        }
   


class ConductorForm(forms.ModelForm):

    class Meta:
        model = Conductor
        fields = "__all__"


        widgets ={
        'activo': forms.TextInput(attrs={'placeholder': '0 = No o 1 = Si'}),



        }

class TransporteForm(forms.ModelForm):

    class Meta:
        model = Transporte
        fields = "__all__"

        
class VehiculoForm(forms.ModelForm):

    class Meta:
        model = Vehiculo
        fields = "__all__"


class FuncionarioForm(forms.ModelForm):

    class Meta:
        model = Funcionario
        fields = "__all__"