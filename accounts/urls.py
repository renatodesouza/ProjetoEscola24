from django.urls import path
from .views import AlunoView


app_name = 'accounts'

urlpatterns = [
    path('aluno/<int:pk>/', AlunoView.as_view(), name='aluno'),
]