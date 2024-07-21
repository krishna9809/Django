from django import template

register = template.Library()

@register.filter(name='multiply')
def multiply(value, arg):
    """Multiplies the value by the argument."""
    try:
        return value * arg
    except TypeError:
        return value

@register.filter(name='to_upper')
def to_upper(value):
    """Converts a string to uppercase."""
    if isinstance(value, str):
        return value.upper()
    return value

