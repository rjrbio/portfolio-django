from django import template

register = template.Library()

@register.filter(name='split')
def split(value, arg):
    """Split a string by a delimiter"""
    return value.split(arg)

@register.filter(name='strip')
def strip(value):
    """Remove leading and trailing whitespace"""
    return value.strip()
