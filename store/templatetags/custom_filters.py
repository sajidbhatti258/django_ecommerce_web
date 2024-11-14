from django import template

register = template.Library()

@register.filter(name='custom_filters')
def custom_filters(value):
    # Implement your filter logic here
    return value.upper()  # Example: converting text to uppercase
