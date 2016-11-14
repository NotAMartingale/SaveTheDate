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
    mensajePareja = RichTextField(blank=True)
    mensajeBoda = RichTextField(blank=True)
    mensajeConfirmacion = RichTextField(blank=True)

    jumboImg1 =  models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+'
    )
    jumboImg2 =  models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+'
    )
    jumboImg3 =  models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+'
    )

    recepcionImg =  models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+'
    )

    footerImg =  models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+'
    )
    subpage_types = ['Localizacion',
                     'GaleriaFotos',
                     'Acomodaciones',
                     'ListaNoviosPage',
                     ]

    content_panels = Page.content_panels + [
        FieldPanel('mensajePareja', classname="full"),
        FieldPanel('mensajeBoda', classname="full"),
        FieldPanel('mensajeConfirmacion', classname="full"),
        ImageChooserPanel('jumboImg1'),
        ImageChooserPanel('jumboImg2'),
        ImageChooserPanel('jumboImg3'),
        ImageChooserPanel('recepcionImg'),
        ImageChooserPanel('footerImg'),
    ]


class Localizacion(Page):
    imagenFondo = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+'
    )
    nombreCompleto = RichTextField(blank=True)
    direccion = RichTextField(blank=True)
    imagenCeremonia = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+'
    )
    descripcionCeremonia = RichTextField(blank=True)
    imagenRecepcion = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+'
    )
    descripcionRecepcion = RichTextField(blank=True)
    localizacion_maps = models.TextField(blank=True)
    content_panels = Page.content_panels + [
        ImageChooserPanel('imagenFondo'),
        ImageChooserPanel('imagenCeremonia'),
        FieldPanel('descripcionCeremonia', classname="full"),
        ImageChooserPanel('imagenRecepcion'),
        FieldPanel('descripcionRecepcion', classname="full"),
        FieldPanel('nombreCompleto', classname="full"),
        FieldPanel('direccion', classname="full"),
        FieldPanel('localizacion_maps', classname="full"),
    ]


class GaleriaFotos(Page):
    imagenFooter = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+'
    )
    mensajeGaleria = RichTextField(blank=True)

    content_panels = Page.content_panels + [
       ImageChooserPanel('imagenFooter'),
       FieldPanel('mensajeGaleria', classname="full"),
    ]


class Acomodaciones(Page):
    imagenHeader = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+'
    )
    mensajeBreve = models.TextField()
    mensajeHoteles = RichTextField(blank=True)
    mensajeRestaurants = RichTextField(blank=True)
    mensajeTurismo = RichTextField(blank=True)
    imagenFooter = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+'
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel('imagenHeader'),
        ImageChooserPanel('imagenFooter'),
        FieldPanel('mensajeBreve', classname="full"),
        FieldPanel('mensajeHoteles', classname="full"),
        FieldPanel('mensajeRestaurants', classname="full"),
        FieldPanel('mensajeTurismo', classname="full"),
    ]


class ListaNoviosPage(Page):
    imagenHeader = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+'
    )
    mensajeBreve = models.TextField()
    mensajeExtendido = RichTextField(blank=True)
    imagenFooter = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+'
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel('imagenHeader'),
        ImageChooserPanel('imagenFooter'),
        FieldPanel('mensajeBreve', classname="full"),
        FieldPanel('mensajeExtendido', classname="full"),
    ]


@register_snippet
class CodigoListaNovio(models.Model):
    logoEmpresa = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+'
    )
    nombreEmpresa = models.CharField(max_length=255)
    descripcion = RichTextField(blank=True)
    nombreCodigo = models.CharField(max_length=255)
    codigo = models.CharField(max_length=255)

    panels = [
        ImageChooserPanel('logoEmpresa'),
        FieldPanel('nombreEmpresa'),
        FieldPanel('descripcion', classname="full"),
        FieldPanel('nombreCodigo'),
        FieldPanel('codigo'),
    ]


@register_snippet
class FotoGaleria(models.Model):
    foto = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+'
    )
    nombre = models.CharField(max_length=255)

    panels = [
        ImageChooserPanel('foto'),
        FieldPanel('nombre'),
    ]


@register_snippet
class InfoNovios(models.Model):
    fotoNovio = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+'
    )
    fotoNovia = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+'
    )

    mensajeNovio = RichTextField(blank=True)
    mensajeNovia = RichTextField(blank=True)

    panels = [
        ImageChooserPanel('fotoNovio'),
        ImageChooserPanel('fotoNovia'),
        FieldPanel('mensajeNovio', classname="full"),
        FieldPanel('mensajeNovia', classname="full"),
    ]


@register_snippet
class Ceremonia(models.Model):
    foto = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+'
    )
    descripcion = RichTextField(blank=True)

    panels = [
        ImageChooserPanel('foto'),
        FieldPanel('descripcion', classname="full"),
    ]


@register_snippet
class Recepcion(models.Model):
    foto = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+'
    )
    descripcion = RichTextField(blank=True)

    panels = [
        ImageChooserPanel('foto'),
        FieldPanel('descripcion', classname="full"),
    ]


@register_snippet
class ListaNovios(models.Model):
    foto = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+'
    )
    descripcion = RichTextField(blank=True)

    panels = [
        ImageChooserPanel('foto'),
        FieldPanel('descripcion', classname="full"),
    ]


@register_snippet
class Hoteles(models.Model):
    foto = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+'
    )
    nombre = models.TextField()
    direccion = models.TextField()
    url = models.TextField()
    descripcion = RichTextField(blank=True)

    panels = [
        ImageChooserPanel('foto'),
        FieldPanel('nombre', classname= "full"),
        FieldPanel('direccion', classname="full"),
        FieldPanel('url', classname="full"),
        FieldPanel('descripcion', classname="full"),
    ]
