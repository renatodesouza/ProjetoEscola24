from django.db import models
from django.contrib.auth.models import User
from .disciplina import Disciplina



class Professor(models.Model):
    rp = models.CharField(max_length=10, unique=True, verbose_name='RP', blank=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name='usuario_professor', verbose_name='Usuario')
    celular = models.CharField('Celular', max_length=20)
    disciplina = models.ManyToManyField(Disciplina, blank=True, related_name='disciplinas_lecionadas')
    imagem = models.ImageField("Imagem", upload_to='imagens/', blank=True)
                                       
    def __str__(self):
        return self.usuario.username