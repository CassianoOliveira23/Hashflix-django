# Generated by Django 4.2.9 on 2024-02-12 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filme', '0003_alter_filme_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filme',
            name='categoria',
            field=models.TextField(choices=[('ACAO', 'Ação'), ('TERROR', 'Terror'), ('COMEDIA', 'Comédia'), ('FANTASIA', 'Fantasia'), ('PROGRAMACAO', 'Programação'), ('SERIES', 'Séries')], max_length=15),
        ),
    ]
