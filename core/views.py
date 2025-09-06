from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from courses.models import Curso
from .forms import LoginForm



class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cursos'] = Curso.objects.order_by('?')[:3]
        context['list_cursos'] = Curso.objects.all()
        context['form'] = LoginForm()
        
        return context


def my_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['usuario']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            print(user.username)
            if user is not None:
                login(request, user)
                if user.is_staff:
                    return redirect('accounts:professor')
                
                return redirect('accounts:aluno', user.id)
            else:
                return redirect('core:home')
    return redirect('core:home')

def my_logout(request):
    logout(request)
    return redirect('core:home')


