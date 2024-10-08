from django.urls import path
from . import views
from .views import HomeView, CursoView, AlunoView, ProfessorView, ProfessorTemplateView, CursoCreateView, EntregaAtividadeView,\
create, delete,cursos, my_login, my_logout, boletim, cria_entrega_atividade, edita_entrega_atividade, MensagemViews
from django.views.generic import TemplateView



app_name = 'app'

urlpatterns = [
    
    path('home/', HomeView.as_view(), name='home'),
    path('curso/<int:pk>/', CursoView.as_view(), name='curso'),
    path('aluno/<int:pk>/', AlunoView.as_view(), name='aluno'),

    path('professor-template/', ProfessorTemplateView.as_view(), name='professor_template'),
    path('professor/<int:pk>/', ProfessorView.as_view(), name='professor'),
    
    path('boletim-aluno/', views.boletim, name='boletim'),
    path('cursos/', views.cursos, name='cursos'),

    path('curso-create/', views.create , name='create'),
    path('curso-delete/<int:pk>/', views.delete, name='delete'),
    path('update/<int:pk>/', views.update, name='update'),
    
    path('login/', views.my_login, name='my_login'),
    path('curso-form/', CursoCreateView.as_view(), name='curso_form_create'),
    
    path('logout/', views.my_logout, name='my_logout'),

    path('cria-entrega-atividade/', EntregaAtividadeView.as_view(), name='cria_entrega_atividade'),
    path('edita-entrega-atividade/', view=edita_entrega_atividade, name='edita_entrega_atividade'),
    path('mensagem/', MensagemViews.as_view(), name='mensagem'),

    
]