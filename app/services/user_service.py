from django.contrib.auth.models import User

from app.models.professor import Professor
from app.models.aluno import Aluno


def get_user_data(usuario):
    """
    Verifica o tipo de usuário (Professor, Coordenador ou Aluno) e retorna os dados associados.
    
    Parâmetros:
    usuario (User): O objeto User do Django que representa o usuário logado.
    
    Retorna:
    tuple: Uma tupla contendo o tipo de usuário (str) e os dados do objeto (Model) correspondente.
    """
    if hasattr(usuario, 'usuario_professor'):
        return 'usuario_professor', Professor.objects.get(usuario=usuario)
    elif hasattr(usuario, 'usuario_aluno'):
        return 'usuario_aluno', Aluno.objects.get(usuario=usuario)
    return None, None