# yourapp/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    """Multiplies the given value by the arg."""
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return ''
