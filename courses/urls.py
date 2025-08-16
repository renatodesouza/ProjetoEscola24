from django.urls import path
from .views import CursoView

app_name = 'courses'

urlpatterns = [
    path('curso/<int:pk>/', CursoView.as_view(), name='curso'),
]