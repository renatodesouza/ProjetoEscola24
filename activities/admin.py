from django.contrib import admin
from .models import Atividade, EntregaAtividade


@admin.register(Atividade)
class AtividadeAdmin(admin.ModelAdmin):

    list_display = ('id', 'titulo', 'descricao', 'status', 'atividade',
                    'dt_inicio', 'dt_fim', 'professor', 'disciplina')
    
    fieldsets = [
        ('Atividade',           {'fields':('titulo', 'descricao', 'atividade', 'status')}),
        ('Professor',           {'fields':('professor',)}),
        ('Disciplina',          {'fields':('disciplina',)}),
        ('Turmas',              {'fields':('turma',)}),
        ('Datas',               {'fields':('dt_inicio', 'dt_fim')})
    ]


    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        
        return queryset.filter(professor__usuario=request.user) or queryset.filter(turma__matricula__aluno__usuario=request.user)
    

@admin.register(EntregaAtividade)
class EntregaAtividadeAdmin(admin.ModelAdmin):

    list_display = ('id', 'atividade', 'aluno', 'professor', 'dt_entrega', 'status',
                    'nota', 'observacao', 'file')
    
    fieldsets = [
        ('Atividade',                       {'fields':('atividade',)}),
        ('Professor',                       {'fields':('professor',)}),
        ('Aluno',                           {'fields':('aluno',)}),
        ('Informações da Atividade',        {'fields':('status', 'resposta', 'file', 'nota')}),
        ('Observação',                      {'fields':('observacao',)})
    ]

    search_fields = ['aluno__usuario__first_name', 'atividade__nome', 'status', 'dt_entrega']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(aluno__usuario=request.user) or queryset.filter(professor__usuario=request.user)
