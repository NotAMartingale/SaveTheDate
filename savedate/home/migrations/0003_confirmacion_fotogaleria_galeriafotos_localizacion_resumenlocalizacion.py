# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-15 21:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0012_copy_image_permissions_to_collections'),
        ('wagtailcore', '0028_merge'),
        ('home', '0002_remove_homepage_jumboimg4'),
    ]

    operations = [
        migrations.CreateModel(
            name='Confirmacion',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('mensajeBreve', models.TextField()),
                ('mensajeExtendido', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('imagenFooter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('imagenHeader', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='FotoGaleria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('foto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
        ),
        migrations.CreateModel(
            name='GaleriaFotos',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('mensajeGaleria', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('imagenFooter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='Localizacion',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('nombreCompleto', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('direccion', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('imagenFondo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ResumenLocalizacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensajeCeremonia', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('mensajeRecepcion', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('ceremoniaFoto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('recepcionFoto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
        ),
    ]