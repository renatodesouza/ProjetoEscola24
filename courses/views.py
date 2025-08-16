from django.shortcuts import render
from django.views.generic import DetailView
from .models import Curso, Turma


class CursoView(DetailView):
    template_name = 'courses/curso.html'
    model = Curso
    context_object_name = 'curso'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cursos'] = Curso.objects.all()
        curso = self.get_object()
        turmas = Turma.objects.filter(curso__nome=curso, turma='TURMA A')

        disciplinas_por_semestre = [
            {'semestre':turma.semestre,
             'disciplinas':turma.disciplina.all()}
             for turma in turmas
        ]

        context['disciplinas_por_semestre'] = disciplinas_por_semestre

        return context