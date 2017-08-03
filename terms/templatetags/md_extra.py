from markdown import markdown

from django import template

register = template.Library()

@register.filter
def md_to_html(value):
	return markdown(value, output_format='html5')
