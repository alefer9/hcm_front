# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-06 20:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_site', '0003_remove_reserva_empleado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('reserva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_site.Reserva')),
            ],
        ),
        migrations.AddField(
            model_name='reserva',
            name='empleado',
            field=models.ManyToManyField(related_name='reserva_requests_created', through='app_site.Solicitud', to=settings.AUTH_USER_MODEL),
        ),
    ]