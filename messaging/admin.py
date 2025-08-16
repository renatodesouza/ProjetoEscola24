from django.contrib import admin
from .models import Mensagem
from django.db.models import Q


@admin.register(Mensagem)
class MensagemAdmin(admin.ModelAdmin):

    list_display = ('remetente', 'destinatario', 'mensagem', 'dt_envio')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        
        return queryset.filter(Q(remetente=request.user) | Q(destinatario=request.user))
