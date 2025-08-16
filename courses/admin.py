from django.contrib import admin
from .models import Curso, Disciplina, Matricula, Turma

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):

    list_display = ('id', 'nome', 'descricao', 'periodo', 'modalidade', 'coordenador', 'imagem')

    fieldsets = [
    ('Informações basicas',             {'fields': ('nome', 'descricao')}),
    ('Horarios',                        {'fields': ('periodo', 'modalidade')}),
    ('Coordenador responsavel',         {'fields':('coordenador',)}),
    ('Imagem',                          {'fields':('imagem',)})
    ]
    
    search_fields = ['nome'] 


@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('id' ,'nome', 'carga_horaria')

    fieldsets = [
        ('Informações da Disciplina',   {'fields':('nome', 'carga_horaria')}),
        ('Cursos',                      {'fields':('curso',)}),
        ('Imagem',                      {'fields':('imagem',)})
    ]

    search_fields = ['nome']
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(turma__matricula__aluno__usuario=request.user) or queryset.filter(professor__usuario=request.user)


@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'curso', 'turma', 'dt_inicio', 'dt_final', 'status')

    fieldsets = [
        ('Informações da matricula',            {'fields':('aluno', 'curso', 'turma',
                                                           'dt_inicio', 'dt_final', 'status')}),
    ]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        print(queryset)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(aluno__usuario=request.user)


@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('id' ,'turma', 'curso', 'semestre')

    fieldsets = [
        ('Informações da turma',       {'fields':('curso', 'turma', 'semestre', 'disciplina')}),
    ]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(disciplina__professor__usuario=request.user) or queryset.filter(matricula__aluno__usuario=request.user)