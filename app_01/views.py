# Imports

from django.shortcuts import render, redirect
from .models import User

# Mostra a página index.html


def home(request):
    users = User.objects.all()
    return render(request, 'index.html', {'users': users})

# Cria o usuário (Create) e exibe eles em uma tabela (Read)


def save(request):
    email_ = request.POST.get("email")
    User.objects.create(email=email_)
    users = User.objects.all()
    return render(request, 'index.html', {'users': users})

# Edita o usuário (Update)


def edit(request, id):
    user = User.objects.get(id=id)
    return render(request, 'update.html', {'user': user})


def update(request, id):
    email_ = request.POST.get("email")
    user = User.objects.get(id=id)
    user.email = email_
    user.save()
    return redirect(home)

# Exclui o usuário (Delete)


def delete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect(home)
