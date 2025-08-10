from django.contrib import admin
from .models import Aluno, Coordenador, Professor


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):

    list_display = ('id', 'ra', 'usuario', 'data_expiracao', 'imagem')

    fieldsets = [
        ('Informações do Aluno',        {'fields':('ra', 'usuario', 'data_expiracao', 'imagem')})
    ]

    search_fields = ['ra']


@admin.register(Coordenador)
class CoordenadorAdmin(admin.ModelAdmin):

    list_display = ('usuario', 'celular')

    fieldsets = [
        ("Informoções do Coordenador",        {'fields': ('usuario', 'celular')})
    ]

    search_fields = ['usuario']


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):

    #form = ProfessorForm

    list_display = ('id', 'usuario', 'celular', 'rp', 'imagem')

    fieldsets = [
        ("Informoções do Professor",        {'fields': ('usuario', 'celular', 'rp', 'imagem')}),
        ("Disciplinas lecionadas",          {'fields':('disciplina',)})
    ]

    search_fields = ['usuario']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(usuario=request.user)