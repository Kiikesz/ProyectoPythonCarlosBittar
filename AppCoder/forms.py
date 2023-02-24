from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 

class  Cursoformulario(forms.Form):
     nombre = forms.CharField(max_length=20)
     camada = forms.IntegerField()
     comision = forms.IntegerField()

class ProfesorFormulario(forms.Form):
    
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=40)
    profesion = forms.CharField(max_length=20)
    edad = forms.IntegerField()

class EntregableFormulario(forms.Form):
        nombre = forms.CharField(max_length=20)
        fecha = forms.DateField()
        entregado = forms.BooleanField()

class formularioestudiante(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=40)

class ResgistroFormulario(UserCreationForm):
     first_name =forms.CharField(label="Nombre")
     last_name = forms.CharField(label="Apellido")
     email = forms.EmailField(label="Correo")
     password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
     password2 = forms.CharField(label="Confirme conrasaeña", widget=forms.PasswordInput)

     class Meta:
          model = User
          fields = ["username", "first_name", "last_name", "email", "password1", "password2"]

