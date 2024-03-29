# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-15 21:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0012_copy_image_permissions_to_collections'),
        ('home', '0003_confirmacion_fotogaleria_galeriafotos_localizacion_resumenlocalizacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodigoListaNovio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreEmpresa', models.CharField(max_length=255)),
                ('descripcion', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('nombreCodigo', models.CharField(max_length=255)),
                ('codigo', models.CharField(max_length=255)),
                ('logoEmpresa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
        ),
    ]
