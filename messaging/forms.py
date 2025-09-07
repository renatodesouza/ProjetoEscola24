
from django import forms
from accounts.models import Aluno, Professor
from messaging.models import Mensagem


class MensagemForm(forms.ModelForm):
    aluno = Aluno.objects.all()
    professor = Professor.objects.all()

    class Meta:
        model = Mensagem
        fields = ['remetente', 'destinatario', 'assunto', 'mensagem']