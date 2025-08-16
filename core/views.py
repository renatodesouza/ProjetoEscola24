from django.shortcuts import render
from django.views.generic import TemplateView
from courses.models import Curso



class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cursos'] = Curso.objects.order_by('?')[:3]
        context['list_cursos'] = Curso.objects.all()
        
        return context
