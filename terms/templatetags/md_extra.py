import re
from markdown import Markdown
from markdown.extensions import meta
from django import template

register = template.Library()

meta.META_RE = re.compile(r'^[ ]{0,3}(?P<key>\w+):\s*(?P<value>.*)')

def get_compiler():
	return Markdown(
		output_format='html5',
		extensions = [meta.MetaExtension(), 'markdown.extensions.nl2br']
	)

@register.filter
def md_to_html(flatpage):
	return get_compiler().convert(flatpage.content)

@register.filter
def extract_meta(flatpage):
	md = get_compiler()
	md.convert(flatpage.content)
	return md.Meta

@register.filter
def publish_url(page_id):
	return '/terms/publish/{}/'.format(page_id)
