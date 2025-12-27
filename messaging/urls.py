from django.urls import path
from .views import MensagemViews


app_name = 'messaging'

urlpatterns = [
    path('mensagem/', MensagemViews.as_view(), name='mensagem'),
]