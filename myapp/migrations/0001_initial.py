# Generated by Django 4.2.4 on 2023-08-01 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Responsavel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Range_salarial', models.CharField(blank=True, choices=[('Até R$ 1.000', 'Até R$ 1.000'), ('R$ 1.001 a R$ 2.000', 'R$ 1.001 a R$ 2.000'), ('R$ 2.001 a R$ 3.000', 'R$ 2.001 a R$ 3.000'), ('R$ 3.001 a R$ 4.000', 'R$ 3.001 a R$ 4.000'), ('R$ 4.001 a R$ 5.000', 'R$ 4.001 a R$ 5.000'), ('R$ 5.001 a R$ 6.000', 'R$ 5.001 a R$ 6.000'), ('R$ 6.001 a R$ 7.000', 'R$ 6.001 a R$ 7.000'), ('R$ 7.001 a R$ 8.000', 'R$ 7.001 a R$ 8.000'), ('R$ 8.001 a R$ 9.000', 'R$ 8.001 a R$ 9.000'), ('R$ 9.001 a R$ 10.000', 'R$ 9.001 a R$ 10.000'), ('R$ 10.001 a R$ 15.000', 'R$ 10.001 a R$ 15.000'), ('R$ 15.001 a R$ 20.000', 'R$ 15.001 a R$ 20.000'), ('R$ 20.001 a R$ 30.000', 'R$ 20.001 a R$ 30.000'), ('R$ 30.001 a R$ 50.000', 'R$ 30.001 a R$ 50.000'), ('Acima de R$ 50.000', 'Acima de R$ 50.000')], max_length=255, null=True)),
                ('Escolaridade', models.CharField(blank=True, choices=[('Fundamental', 'Ensino Fundamental'), ('Medio', 'Ensino Médio'), ('Superior', 'Ensino Superior'), ('PosGraduacao', 'Pós-Graduação'), ('Mestrado', 'Mestrado'), ('Doutorado', 'Doutorado')], max_length=255, null=True)),
            ],
        ),
    ]