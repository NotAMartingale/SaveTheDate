from __future__ import unicode_literals

from django.db import models

from wagtail.wagtaildocs.edit_handlers import DocumentChooserPanel
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailsearch import index
from wagtail.wagtailsnippets.models import register_snippet

class HomePage(Page):
    mensajeNupcias = models.CharField(max_length=255)
    nombreNovio = models.CharField(max_length=255)
    nombreNovia = models.CharField(max_length=255)
    fechaMatrimonio = models.CharField(max_length=255)
    hora = models.CharField(max_length=255)
    ubicacion = models.CharField(max_length=255)
    fotoBackground = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('mensajeNupcias'),
        FieldPanel('nombreNovio'),
        FieldPanel('nombreNovia'),
        FieldPanel('fechaMatrimonio'),
        FieldPanel('hora'),
        FieldPanel('ubicacion'),
        ImageChooserPanel('fotoBackground'),
    ]


@register_snippet
class InfoNovios(models.Model):
    foto = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+'
    )
    titulo = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    descripcion = RichTextField(blank=True)

    panels = [
        ImageChooserPanel('foto'),
        FieldPanel('titulo'),
        FieldPanel('nombre'),
        FieldPanel('BriefDescription', classname="full"),
    ]