from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Mensagem
from .forms import MensagemForm

class MensagemViews(CreateView):
    template_name = 'app/partials/_nova_mensagem.html'
    model = Mensagem
    
    form_class = MensagemForm
    success_url = reverse_lazy('accounts:aluno')

    def get_context_data(self, **kwargs):
        context = super(MensagemViews, self).get_context_data(**kwargs)
        
        context['mensagem_form'] = MensagemForm()
        context['mensagens'] = Mensagem.objects.all()
        return context

    def post(self, request, **kwargs):
        if request.method == 'POST':
            mensagem_form = MensagemForm(request.POST)
            
            if mensagem_form.is_valid():
                remetente = get_object_or_404(User, pk=mensagem_form.cleaned_data['remetente'].id)
                destinatario = get_object_or_404(User, pk=mensagem_form.cleaned_data['destinatario'].id)

                assunto = mensagem_form.cleaned_data['assunto']
                mensagem = mensagem_form.cleaned_data['mensagem']
                data_envio = timezone.now()
                
                Mensagem.objects.create(remetente=remetente, destinatario=destinatario,
                                         assunto=assunto, mensagem=mensagem, dt_envio=data_envio)
                

                
            return redirect('accounts:aluno', self.request.user.id)
        return redirect('accounts:aluno', self.request.user.id)
