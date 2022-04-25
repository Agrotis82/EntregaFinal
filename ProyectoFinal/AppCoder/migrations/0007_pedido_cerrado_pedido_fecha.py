# Generated by Django 4.0.3 on 2022-04-19 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0006_pedido_temp'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='cerrado',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='pedido',
            name='fecha',
            field=models.DateField(blank=True, null=True, verbose_name='fecha'),
        ),
    ]
