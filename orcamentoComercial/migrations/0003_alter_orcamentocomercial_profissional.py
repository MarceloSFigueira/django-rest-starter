# Generated by Django 5.0.1 on 2024-07-03 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orcamentoComercial', '0002_alter_orcamentocomercial_area_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orcamentocomercial',
            name='profissional',
            field=models.CharField(max_length=100),
        ),
    ]
