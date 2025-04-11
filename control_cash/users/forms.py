from django import forms
from django.contrib.auth.models import User
from .models import *

class UsersRegisterForm(forms.ModelForm):
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password_confirm = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            
        }

    def clean_password_confirm(self):
        clean_data = self.cleaned_data
        if clean_data['password'] != clean_data['password_confirm']:
            raise forms.ValidationError('Las contraseñas no coinciden')
        else:
            return clean_data['password']
        
