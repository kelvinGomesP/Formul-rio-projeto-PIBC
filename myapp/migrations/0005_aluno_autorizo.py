# Generated by Django 4.2.4 on 2023-08-01 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_rename_matricula_aluno_matrícula'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='Autorizo',
            field=models.BooleanField(default=False),
        ),
    ]
