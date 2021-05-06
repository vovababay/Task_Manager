from django import template
from django.urls import reverse_lazy

from board.models import *

register = template.Library()


@register.simple_tag
def create_new_column(name):
    Column.objects.create(name=name)
    return reverse_lazy("home")
