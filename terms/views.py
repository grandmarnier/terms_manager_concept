from django.contrib import messages
from django.contrib.flatpages.models import FlatPage
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string


def publish(request, page_id):
	try:
		page = FlatPage.objects.get(pk=page_id)
	except ObjectDoesNotExist:
		messages.add_message(request, messages.ERROR,
							 'Page not found')
	else:
		html = render_to_string(page.template_name, {'flatpage': page})
		file_name = 'media/{}.html'.format(page.title.strip('/'))
		with open(file_name, 'w') as f:
			f.write(html)

		messages.add_message(request, messages.INFO,
							 'Terms are published at {}.'.format(file_name))

	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
