from django import template
import sethub.views as views

register = template.Library()

@register.simple_tag()
def get_categories():
    return views.cats_db