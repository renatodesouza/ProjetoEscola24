# Generated by Django 3.2 on 2024-10-02 00:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_auto_20241001_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matricula',
            name='aluno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='aluno_matricula', to='app.aluno'),
        ),
        migrations.AlterField(
            model_name='matricula',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='curso_matricula', to='app.curso'),
        ),
        migrations.AlterField(
            model_name='matricula',
            name='turma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='turma_matricula', to='app.turma'),
        ),
    ]
