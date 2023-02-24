from django.urls import path
from AppCoder.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('inicio/', inicio, name="Start"),
    path('ver_estudiantes/', Estudiantes, name="ver estudiantes"),
    path('ver_entregables/', Entregables, name="ver entregables"),
    path('ver_cursos/', Cursos, name="ver cursos"),
    path('ver_profesores/', Profesores, name="ver porfesores"),
    path('crear_estudiante/', crear_estudiante , name='crear estudiante'),
    path('crear_curso/', crear_curso, name='crear curso'),
    path('crear_profesor/', crear_profesor, name='crear profesor'),
    path('crear_entregables/', crear_entregable, name='crear entregable'),
    path('resultado/', busquedacursos, name='resultado busqueda'),
    path('resultado_entregable/', resultado_entregable , name='resultado entregable'),
    path('resultado_estudiante/', resultado_estudiante  , name='resultado estudiante'),
    path('resultado_profesor/', resultado_profesor, name='resultado profesor'),
    path('borrar_profe/<profesor_email>', borrar_profesor, name='Borrar Profesor'),
    path('borrar_estudiante/<estudiante_email>', borrar_estudiante, name='Borrar Estudiante'),
    path('borrar_curso/<curso_comision>', borrar_curso, name='Borrar Curso'),
    path('borrar_entregable/<entregable_nombre>', borrar_entregable , name='Borrar Entregable'),
    path('editar_profesor/<profesor_email>', editar_profesor , name='Editar Profesor'),
    path('editar_curso/<curso_comision>', editar_curso , name='Editar Curso'),
    path('editar_entregable/<nombre_entregable>', editar_entregable , name='Editar Entregable'),
    path('editar_estudiante/<estudiante_email>', editar_estudiante , name='Editar Estudiante'),
    path('registro/', registro , name='registro'),
    path('login/', iniciar_sesion , name='Sign In'),
    path('logout/', LogoutView.as_view(template_name = "AppCoder/logout.html"), name ="Logout" )
]