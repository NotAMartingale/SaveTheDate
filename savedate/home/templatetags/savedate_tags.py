from django import template

from ..models import InfoNovios
from ..models import Ceremonia
from ..models import Recepcion
from ..models import ListaNovios
from ..models import FotoGaleria
from ..models import CodigoListaNovio
from ..models import Hoteles

register = template.Library()

@register.inclusion_tag('tags/informacion_novios.html')
def informacion_novios():
    infoNovios = InfoNovios.objects.all()[0]
    return {'infoNovios': infoNovios}


@register.inclusion_tag('tags/informacion_general.html')
def informacion_general():
    ceremonia = Ceremonia.objects.all()[0]
    recepcion = Recepcion.objects.all()[0]
    listaNovios = ListaNovios.objects.all()[0]
    return {'ceremonia': ceremonia,
            'recepcion': recepcion,
            'listaNovios': listaNovios}


@register.inclusion_tag('tags/slider_galeria.html')
def slider_galeria():
    fotos = FotoGaleria.objects.all()
    return {'fotos': fotos}


@register.inclusion_tag('tags/fotos_galeria.html')
def fotos_galeria():
    fotos = FotoGaleria.objects.all()
    return {'fotos': fotos}


@register.inclusion_tag('tags/codigos_novios.html')
def codigos_novios():
    codigos = CodigoListaNovio.objects.all()
    return {'codigos': codigos}


@register.inclusion_tag('tags/info_codigos_novios.html')
def info_codigos_novios():
    codigos = CodigoListaNovio.objects.all()
    return {'codigos': codigos}


@register.inclusion_tag('tags/info_hoteles.html')
def info_hoteles():
    hoteles = Hoteles.objects.all()
    return {'hoteles': hoteles}