from django import forms
from accounts.models import Professor
from courses.models import Disciplina
from activities.models import EntregaAtividade, Atividade



class AtividadeForm(forms.ModelForm):
    class Meta:
        model = Atividade
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        professor = kwargs.pop('professor')
        super().__init__(*args, **kwargs)
        self.order_fields['disciplina'].queryset = Disciplina.objects.filter(professor=professor)

class EntregaAtividadeForm(forms.ModelForm):
    professores = Professor.objects.all()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if not self.instance._state.adding and not self.instance.aluno.has_perm('app.alterar_nota'):
            self.fields['nota'].disabled = True

        class Meta:
            model = EntregaAtividade
            fields = '__all__'

        resposta = forms.CharField(
        label = 'Resposta',
        max_length=500,

        widget=forms.Textarea(
            attrs={
                'resposta':'resposta',
            }
        )
    )

    professor = forms.ModelChoiceField(
        queryset=professores,
        empty_label='Selecione um professor',
        label='Professor',
        required=True,
        widget=forms.Select(
            attrs={
                'class':'form-control',
                'professor':'professor',
                'data-value':'professor.id'

            }
        )
    )

    def clean_campo_limitado(self):
        nota = self.cleaned_data['nota']

        return nota