from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from accounts.models import Aluno, Coordenador, Professor
from courses.models import Matricula, Curso, Disciplina, Turma
from messaging.models import Mensagem
from activities.models import EntregaAtividade, Atividade
from activities.forms import EntregaAtividadeForm


class AlunoView(DetailView):
    model = Aluno
    template_name = 'accounts/aluno.html'
    context_object_name = 'user'

    def get_queryset(self):
        self.nome = get_object_or_404(User, pk=self.kwargs['pk'])
        return User.objects.filter(id=self.nome.id)
    
    def get_context_data(self, **kwargs):

        usuario = self.request.user
        matricula = Matricula.objects.get(aluno__usuario=usuario)
        atividades = matricula.turma.turma_atividades.all()

        context = super().get_context_data(**kwargs)

        context['aluno'] = Aluno.objects.get(usuario=usuario)
        context['cursos'] = Curso.objects.all()
        context['turma'] = matricula.turma
        context['semestre'] = Turma.objects.all()
        context['curso'] = matricula.curso
        context['disciplinas'] = matricula.turma.disciplina.all()
        context['atividades'] = atividades
        context['atividades_limit'] = atividades.order_by('?')[:3]
        
        context['professores'] = Professor.objects.all()
        context['mensagens'] = Mensagem.objects.filter(remetente=usuario.id).order_by('?')[:3]
        context['mensagens_recebidas'] = Mensagem.objects.filter(destinatario=usuario)
        context['entrega_form'] = EntregaAtividadeForm()

        entregas = EntregaAtividade.objects.filter(aluno__usuario=usuario, atividade__in=context['atividades'])
        atividades_entregues = set(entrega.atividade for entrega in entregas)
        
        context['atividades_entregues'] = atividades_entregues
        context['entregas'] = entregas
        
        return context
    
class ProfessorView(DetailView):
    template_name = 'app/professor.html'

    model = Professor

    def get_queryset(self):
        self.usuario = get_object_or_404(User, pk=self.kwargs['pk'])

        return Professor.objects.filter(usuario=self.usuario)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['professor'] = Professor.objects.get(usuario=self.usuario)
        
        return context