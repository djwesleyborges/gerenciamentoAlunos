from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from alunos.models import Instituicao, Aluno


def index(request):
    alunos = Aluno.objects.get()
    context = {'aluno': alunos}
    return render(request,template_name='index.html',context=context)


def login(request):
    if request.method == "GET":
        form_login = AuthenticationForm()
        return render(request, 'registration/login.html', {'form_login': form_login})

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            alunos = Aluno.objects.get(username=usuario)
            context = {'aluno': alunos}
            return render(request, template_name='index.html', context=context)
        else:
            form_login = AuthenticationForm()
            return render(request, 'registration/login.html', {'form_login': form_login})