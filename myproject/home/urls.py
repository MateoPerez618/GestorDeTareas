from django.urls import path
from .views import registro, home, login_view, registrar_tarea, actualizar_tarea, eliminar_tarea
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("registro/", registro, name="registro"),
    path("home", home, name="home"),
    path('login/', login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registrar_tarea/', registrar_tarea, name='registrar_tarea'),
    path('tarea/<int:pk>/actualizar_tarea/', actualizar_tarea, name='actualizar_tarea'),
    path('tarea/<int:pk>/eliminar/', eliminar_tarea, name='eliminar_tarea'),
]