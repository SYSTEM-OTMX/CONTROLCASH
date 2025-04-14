from django import forms
from django.contrib.auth.models import User
from .models import *

class LoginForm(forms.Form):
    
    username = forms.CharField(
        label='Nombre de Usuario',
        widget=forms.TextInput( attrs={'class':'form-control'})
    )
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput( attrs={'class':'form-control'} )
    )


class UsersRegisterForm(forms.ModelForm):
    password = forms.CharField(
        label="Contraseña", 
        widget=forms.PasswordInput( attrs={'class':'form-control'} ) 
    )
    password_confirm = forms.CharField(
        label="Confirmar contraseña", 
        widget=forms.PasswordInput(attrs={'class':'form-control'})
    )

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
        
