from django.utils.safestring import mark_safe
from django.template import Library
from django.utils.encoding import force_text
import re
import json


register = Library()


@register.filter(is_safe=True)
def intpoint(value):
    """
    Converts an integer to a string containing commas every three
digits.
    For example, 3000 becomes '3,000' and 45000 becomes '45,000'.
    """
    orig = force_text(value)
    new = re.sub("^(-?\d+)(\d{3})", '\g<1>.\g<2>', orig)
    if orig == new:
        return new
    else:
        return intpoint(new)
