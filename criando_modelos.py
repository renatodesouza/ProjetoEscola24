import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')

import django

django.setup()

from app.models.curso import Curso
from app.models.coordenador import Coordenador

coordenador = Coordenador.objects.get(id=1)

print(coordenador.usuario)