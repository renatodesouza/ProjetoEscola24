from django.urls import path
from .views import AlunoView, ProfessorView


app_name = 'accounts'

urlpatterns = [
    path('aluno/<int:pk>/', AlunoView.as_view(), name='aluno'),
    path('professor/<int:pk>/', ProfessorView.as_view, name='professor'),
]