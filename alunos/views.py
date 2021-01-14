from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
#from alunos.forms import CadastrarAlunoForm
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
            alunos = Aluno.objects.get(user=usuario)
            context = {'aluno': alunos}
            return render(request, template_name='index.html', context=context)
        else:
            form_login = AuthenticationForm()
            return render(request, 'registration/login.html', {'form_login': form_login})


# class CadastrarAlunoView(TemplateView):
#     template_name = 'registration/registrar.html'
#
#     def get(self, request):
#         form = CadastrarAlunoForm()
#         context = {'form': form}
#         return render(request, self.template_name, context)
#
#     def post(self, request):
#         form = CadastrarAlunoForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             raw_password = form.cleaned_data.get('password')  # password criptografado
#             user = authenticate(username=user.username, password=raw_password)
#             login(request, user)
#             return redirect('/')
#         args = {'form': form}
#         return render(request, self.template_name, args)