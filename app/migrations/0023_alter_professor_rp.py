# Generated by Django 3.2 on 2024-06-08 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_auto_20240608_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='rp',
            field=models.CharField(blank=True, max_length=10, unique=True, verbose_name='RP'),
        ),
    ]
