from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *
from django.template import Template, Context
from AppCoder.forms import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, UserCreationForm

# Create your views here.


###Viculos HTML###
def inicio(request):

    return render(request,"AppCoder/inicio.html")

def Estudiantes(request):

    return render(request,"AppCoder/ver_estudiantes.html")

def Profesores(request):

    return render(request,"AppCoder/ver_profes.html")

def Entregables(request):

    return render(request,"AppCoder/ver_entregables.html")

def Cursos(request):

    return render(request,"AppCoder/ver_cursos.html")


### Creación #####

def crear_estudiante(request):
    if request.method == 'POST':
        miformulario4 =  formularioestudiante(request.POST)
        if miformulario4.is_valid():
            infodict = miformulario4.cleaned_data
            estu1= Estudiante(nombre=infodict["nombre"], apellido = infodict["apellido"], email = infodict["email"])
            estu1.save()
            return render(request,"AppCoder/inicio.html")
    else:
        miformulario4 = formularioestudiante()
    return render(request,"AppCoder/crear_estudiante.html", {"formulariestudiante":miformulario4})



def crear_curso(request):
    if request.method == 'POST':
        miformulario =  Cursoformulario(request.POST)
        if miformulario.is_valid():
            infodict = miformulario.cleaned_data
            curso1= Curso(nombre=infodict["nombre"], camada = infodict["camada"], comision= infodict["comision"])
            curso1.save()
            return render(request,"AppCoder/inicio.html")
    else:
        miformulario = Cursoformulario()
    return render(request,"AppCoder/crear_curso.html", {"formulariocurso":miformulario})


def crear_profesor(request):
    if request.method == 'POST':
        miformulario1 =  ProfesorFormulario(request.POST)
        if miformulario1.is_valid():
            infodict = miformulario1.cleaned_data
            profe1= Profesor(nombre=infodict["nombre"], apellido = infodict["apellido"], email= infodict["email"], profesion= infodict["profesion"], edad= infodict["edad"],)
            profe1.save()
            return render(request,"AppCoder/inicio.html")
    else:
        miformulario1 = ProfesorFormulario()
    return render(request,"AppCoder/crear_profesor.html", {"formularioprofesor":miformulario1})


def crear_entregable(request):
    if request.method == 'POST':
        miformulario3 =  EntregableFormulario(request.POST)
        if miformulario3.is_valid():
            infodict = miformulario3.cleaned_data
            entre1= Entregable(nombre=infodict["nombre"], fecha = infodict["fecha"], entregado = infodict["entregado"])
            entre1.save()
            return render(request,"AppCoder/inicio.html")
    else:
        miformulario3 = EntregableFormulario()
    return render(request,"AppCoder/crear_entregable.html", {"formularioentregable":miformulario3})



### Busquedas ###

def busquedacursos(request):

    if request.method =="GET":
        busquedacomision = request.GET["comision"]
        comisionresultado = Curso.objects.filter(comision__icontains=busquedacomision)
        return render(request,"AppCoder/resultado.html", {"comision":busquedacomision, "resultados":comisionresultado})
    
    return render(request, "AppCoder/ver_curso.html")

def resultado_entregable(request):

    if request.method =="GET":
        busquedaentregable = request.GET["nombre"]
        entregableresultado = Entregable.objects.filter(nombre__icontains=busquedaentregable)
        return render(request,"AppCoder/resultado_entregable.html", {"nombre":busquedaentregable, "resultados":entregableresultado})
    
    return render(request, "AppCoder/ver_entregables.html")

def resultado_estudiante(request):

    if request.method =="GET":
        busquedaestudiante = request.GET["email"]
        estudianteresultado = Estudiante.objects.filter(email__icontains=busquedaestudiante)
        return render(request,"AppCoder/resultado_estudiante.html", {"email":busquedaestudiante, "resultados":estudianteresultado})
    
    return render(request, "AppCoder/ver_estudiantes.html")

def resultado_profesor(request):

    if request.method =="GET":
        busquedaprofesor = request.GET["email"]
        proferesultado = Profesor.objects.filter(email__icontains=busquedaprofesor)
        return render(request,"AppCoder/resultado_profesor.html", {"email":busquedaprofesor, "resultados":proferesultado})
    
    return render(request, "AppCoder/ver_profesor.html")


### Borrar Registros ###


def borrar_estudiante(request, estudiante_email):
    estudiante_elegido = Estudiante.objects.get(email=estudiante_email)
    estudiante_elegido.delete()
    return render(request, "AppCoder/borrar.html")


def borrar_curso(request, curso_comision):
    comision_elegida = Curso.objects.get(comision=curso_comision)
    comision_elegida.delete()
    return render(request, "AppCoder/borrar.html")


def borrar_entregable(request, entregable_nombre):
    entregable_elegido = Entregable.objects.get(nombre=entregable_nombre)
    entregable_elegido.delete()
    return render(request, "AppCoder/borrar.html")


def borrar_profesor(request, profesor_email):
    profesor_elegido = Profesor.objects.get(email=profesor_email)
    profesor_elegido.delete()
    return render(request, "AppCoder/borrar.html")


### Editar Registros ###

def editar_profesor(request, profesor_email):
    profesor_elegido = Profesor.objects.get(email=profesor_email)
    if request.method == 'POST':
        miformulario1 =  ProfesorFormulario(request.POST)
        if miformulario1.is_valid():
            infodict = miformulario1.cleaned_data
            profesor_elegido.nombre = infodict["nombre"]
            profesor_elegido.apellido = infodict["apellido"]
            profesor_elegido.email = infodict["email"]
            profesor_elegido.profesion = infodict["profesion"]
            profesor_elegido.edad =infodict["edad"]
            profesor_elegido.save()
            return render(request,"AppCoder/inicio.html")
    else:
        miformulario1 = ProfesorFormulario(initial={"nombre": profesor_elegido.nombre,
                                                    "apellido" : profesor_elegido.apellido,
                                                    "email": profesor_elegido.email,
                                                    "profesion": profesor_elegido.profesion,
                                                    "edad": profesor_elegido.edad})
    return render(request,"AppCoder/editar_profesor.html", {"formularioprofesor":miformulario1})



def editar_curso(request, curso_comision):
    curso_elegido = Curso.objects.get(comision=curso_comision)
    if request.method == 'POST':
        miformulario1 =  Cursoformulario(request.POST)
        if miformulario1.is_valid():
            infodict = miformulario1.cleaned_data
            curso_elegido.nombre = infodict["nombre"]
            curso_elegido.camada = infodict["camada"]
            curso_elegido.comision = infodict["comision"]
            curso_elegido.save()
            return render(request,"AppCoder/inicio.html")
    else:
        miformulario1 = Cursoformulario(initial={"nombre": curso_elegido.nombre,
                                                    "camada" : curso_elegido.camada,
                                                    "comision": curso_elegido.comision,})
    return render(request,"AppCoder/editar_curso.html", {"formulariocurso":miformulario1})


def editar_entregable(request, nombre_entregable):
    entregable_elegido = Entregable.objects.get(nombre=nombre_entregable)
    if request.method == 'POST':
        miformulario1 =  EntregableFormulario(request.POST)
        if miformulario1.is_valid():
            infodict = miformulario1.cleaned_data
            entregable_elegido.nombre = infodict["nombre"]
            entregable_elegido.fecha = infodict["fecha"]
            entregable_elegido.entregado = infodict["entregado"]
            entregable_elegido.save()
            return render(request,"AppCoder/inicio.html")
    else:
        miformulario1 = EntregableFormulario(initial={"nombre": entregable_elegido.nombre,
                                                    "fecha" : entregable_elegido.fecha,
                                                    "entregado": entregable_elegido.entregado,})
    return render(request,"AppCoder/editar_entregable.html", {"formularioentregable":miformulario1})


def editar_estudiante(request, estudiante_email):
    estudiante_elegido = Estudiante.objects.get(email=estudiante_email)
    if request.method == 'POST':
        miformulario1 =  formularioestudiante(request.POST)
        if miformulario1.is_valid():
            infodict = miformulario1.cleaned_data
            estudiante_elegido.nombre = infodict["nombre"]
            estudiante_elegido.apellido = infodict["apellido"]
            estudiante_elegido.email = infodict["email"]
            estudiante_elegido.save()
            return render(request,"AppCoder/inicio.html")
    else:
        miformulario1 = formularioestudiante(initial={"nombre": estudiante_elegido.nombre,
                                                    "apellido" : estudiante_elegido.apellido,
                                                    "email": estudiante_elegido.email,})
    return render(request,"AppCoder/editar_estudiante.html", {"formulariestudiante":miformulario1})




###### registro de usuarios


def registro(request):
    if request.method =="POST":
        miformulario = ResgistroFormulario(request.POST)
        if miformulario.is_valid():
            miformulario.save()
            return render(request, "AppCoder/inicio.html")
    else:
        miformulario= ResgistroFormulario()
    return render(request, "AppCoder/registro.html", {"miformulario":miformulario})


### Iniciar sesión 

def iniciar_sesion(request):
    if request.method == "POST":
        miFormulario = AuthenticationForm( request, data = request.POST)
        if miFormulario.is_valid():
            usuario = miFormulario.cleaned_data.get("username")
            contra = miFormulario.cleaned_data.get("password")
            miUsuario = authenticate(username=usuario, password = contra)
            if miUsuario:
                login(request, miUsuario)
                mensaje = f"bienvenido {miUsuario}"
            return render(request, "AppCoder/inicio.html", {"mensaje":mensaje})
        else:
            mensaje = "error al ingresar los datos"
            return render(request, "AppCoder/inicio.html", {"mensaje":mensaje})
    else:
        miFormulario = AuthenticationForm()
    return render(request, "AppCoder/login.html", {"miFormulario":miFormulario})