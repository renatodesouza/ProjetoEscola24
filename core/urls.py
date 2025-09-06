from django.urls import path
from .views import HomeView, my_login, my_logout

app_name = 'core'

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('login/', my_login, name='my_login'),
    path('logout/', my_logout, name='my_logout'),
]