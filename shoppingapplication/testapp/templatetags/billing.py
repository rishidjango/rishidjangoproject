from django import template
register=template.Library()
@register.simple_tag
def mul(a,b):
    return a*b
