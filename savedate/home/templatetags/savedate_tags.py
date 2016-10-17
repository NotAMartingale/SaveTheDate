from django import template

from ..models import InfoNovios
from ..models import Ceremonia
from ..models import Recepcion
from ..models import ListaNovios

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

