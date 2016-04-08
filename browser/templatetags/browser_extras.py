from django import template

register = template.Library()

@register.filter
def to_kg(value):
    return value/1000

@register.filter
def to_liter(value):
    return value/1000
