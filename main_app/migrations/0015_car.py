# Generated by Django 3.2.6 on 2021-11-21 01:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_order_workers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numbers', models.CharField(max_length=50, verbose_name='Номера')),
                ('model', models.CharField(max_length=50, verbose_name='Марка, модель')),
                ('color', models.CharField(blank=True, max_length=50, verbose_name='Цвет')),
                ('worker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cars', to='main_app.worker', verbose_name='Работник')),
            ],
            options={
                'verbose_name': 'Работник',
                'verbose_name_plural': 'Работники',
            },
        ),
    ]
