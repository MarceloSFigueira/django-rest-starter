# Generated by Django 5.0.1 on 2024-07-03 02:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orcamentoComercial', '0004_alter_orcamentocomercial_profissional'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('senioridade', models.CharField(max_length=40)),
                ('salario', models.CharField(max_length=40)),
            ],
        ),
        migrations.RemoveField(
            model_name='orcamentocomercial',
            name='profissional',
        ),
        migrations.RemoveField(
            model_name='orcamentocomercial',
            name='senioridade',
        ),
        migrations.AddField(
            model_name='orcamentocomercial',
            name='cargo',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.DO_NOTHING, to='orcamentoComercial.cargo'),
            preserve_default=False,
        ),
    ]
