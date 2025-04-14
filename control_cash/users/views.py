from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from . import forms
from . import models

def user_login(request):
    if request.method == 'POST':
        user_form = forms.LoginForm(request.POST)
        if user_form.is_valid():
            cleaned_data = user_form.cleaned_data
            user = authenticate(request, username = cleaned_data['username'], password = cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Usuario autenticado')
                else:
                    return HttpResponse('Usuario inactivo')
            else:
                return HttpResponse('El usuario no existe')
        else:
            return HttpResponse('Formulario invalido')
    else:
        form = forms.LoginForm()

        return render(request,'registration') 

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

def register(request):
    data = {}
    if request.method == 'POST':
        user_form = forms.UsersRegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            models.Profile.objects.create(
                user = new_user
            )
            return render(request,'register_done.html')
        else:
            
            data = {
                'user_form':user_form
            }
            return render(request,'register.html',data)
    else:
        user_form = forms.UsersRegisterForm()
        data = {
            'user_form':user_form
        }
        return render(request,'register.html',data)