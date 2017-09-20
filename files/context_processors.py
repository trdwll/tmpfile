from django.conf import settings

def global_settings(request):
	return {
		'MY_HOST_DOMAIN': settings.MY_HOST_DOMAIN,
	}