# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-05 04:47
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20161102_0522'),
    ]

    operations = [
        migrations.AddField(
            model_name='localizacion',
            name='descripcionCeremonia',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='localizacion',
            name='descripcionRecepcion',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
    ]
