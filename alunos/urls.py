from django.urls import path, include

from alunos import views
# from alunos.views import CadastrarAlunoView

urlpatterns = [
    path('', views.login, name='login'),
    path('index/', views.index, name='index'),
    # path('cadastrarAluno/', CadastrarAlunoView.as_view(), name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
]