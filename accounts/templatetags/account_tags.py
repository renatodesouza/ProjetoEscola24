from django import template
from django.templatetags.static import static


register = template.Library()

@register.filter(name='get_avatar')
def get_avatar(user):
    """
    Retorna a URL da imagem do ALuno ou Professor,
    ou uma imagem padrão se não tiver foto ou perfil
    """

    img_url = None

    # Tenta pegar a imagem do Aluno
    # hasattr verifica se o relacionamento existe (se o usário é um aluno)
    if hasattr(user, 'usuario_aluno') and user.usuario_aluno.imagem:
        img_url = user.usuario_aluno.imagem.url

    # Tenta pegar a imagem do professor
    elif hasattr(user, 'usuario_professor') and user.professor.imagem:
        img_url = user.professor.imagem.url

    # retorna a imagem se a encontrou
    if img_url:
        return img_url
    
    # Se não achou nada retorna uma imagem padrão
    return static('img/default-user.png' \
    '')