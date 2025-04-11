from django.shortcuts import render
from . import forms

def register(request):
    data = {}
    if request.method == 'POST':
        pass
    else:
        user_form = forms.UsersRegisterForm()
        data = {
            'user_form':user_form
        }
        return render(request,'register.html',data)