# Generated by Django 5.0.1 on 2024-07-03 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orcamentoComercial', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orcamentocomercial',
            name='area',
            field=models.CharField(choices=[('analytics', 'Analytics'), ('desenvolvimento', 'Desenvolvimento'), ('gestao', 'Gestão')], max_length=40),
        ),
        migrations.AlterField(
            model_name='orcamentocomercial',
            name='forma_pagamento',
            field=models.CharField(choices=[('pre_pago', 'Pré Pago'), ('30_dias', '30 dias'), ('60_dias', '60 dias'), ('90_dias', '90 dias')], max_length=40),
        ),
        migrations.AlterField(
            model_name='orcamentocomercial',
            name='margem',
            field=models.DecimalField(decimal_places=2, default=10.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='orcamentocomercial',
            name='profissional',
            field=models.CharField(choices=[('desenvolvedor', 'Desenvolvedor'), ('analista_dados', 'Analista de Dados')], max_length=40),
        ),
        migrations.AlterField(
            model_name='orcamentocomercial',
            name='senioridade',
            field=models.CharField(choices=[('junior', 'Junior'), ('pleno', 'Pleno'), ('senior', 'Senior'), ('especialista', 'Especialista'), ('coordenador', 'Coordenador'), ('tech_lead', 'Tech Lead')], max_length=40),
        ),
    ]