# Generated by Django 4.0.3 on 2022-04-19 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0005_alter_pedido_idarticulo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido_temp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idcliente', models.IntegerField(verbose_name='idcliente')),
                ('cantidad', models.IntegerField(default='0', verbose_name='cantidad')),
                ('cerrado', models.BooleanField(default=False)),
                ('fecha', models.DateField(verbose_name='fecha')),
                ('idarticulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppCoder.articulos')),
            ],
        ),
    ]