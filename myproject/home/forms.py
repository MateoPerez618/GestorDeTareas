from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, AuthenticationForm
from .models import Tarea

class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "username", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'placeholder': 'Nombre', 'class': 'input-field'})
        self.fields['username'].widget.attrs.update({'placeholder': 'Nombre de usuario', 'class': 'input-field'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Correo electrónico', 'class': 'input-field'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Contraseña', 'class': 'input-field'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirmar contraseña', 'class': 'input-field'})

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Nombre de usuario',
        'class': 'input-field'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Contraseña',
        'class': 'input-field'
    }))

class TareaForm(forms.ModelForm):
    completar_tarea = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Tarea
        fields = ['nombre_tarea', 'descripcion_tarea', 'completar_tarea']