# Generated by Django 4.0.4 on 2022-04-20 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0012_remove_pedido_detalle'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(verbose_name='cantidad')),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppCoder.articulos')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppCoder.pedido')),
            ],
        ),
    ]