from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserForm, LoginForm, TareaForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Tarea

def registro(request):
    data = {
        "form": CustomUserForm()
    }

    if request.method == "POST":
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            user = formulario.save()
            username = formulario.cleaned_data["username"]
            password = formulario.cleaned_data["password1"]
            user = authenticate(username=user.username, password=password)
            login(request, user)
            return redirect("home")

    return render(request, "registro.html", data)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Cambia 'home' por la URL de tu página de inicio
            else:
                messages.error(request, 'Nombre de usuario o contraseña incorrectos')
        else:
            messages.error(request, 'Datos inválidos')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def registrar_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.user = request.user  # Asigna el usuario autenticado
            tarea.save()
            return redirect('home')  # Redirige a la página principal después de guardar la tarea
    else:
        form = TareaForm()
    return render(request, 'tareas.html', {'form': form})

@login_required
def home(request):
    tareas = Tarea.objects.filter(user=request.user)
    return render(request, 'home.html', {'tareas': tareas})

@login_required
def actualizar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirige a la vista de tareas
    else:
        form = TareaForm(instance=tarea)
    return render(request, 'actualizar_tarea.html', {'form': form})

@login_required
def eliminar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk, user=request.user)
    if request.method == 'POST':
        tarea.delete()
        return redirect('home')  # Redirige a la vista de tareas
    return render(request, 'eliminar_tarea.html', {'tarea': tarea})