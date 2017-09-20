import os, random
from .utils import get_checksums

from django.http import JsonResponse
from django.shortcuts import render
from django.utils.crypto import get_random_string
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.conf import settings

from hurry.filesize import size, alternative


@method_decorator(csrf_exempt, name='dispatch')
class HomeView(View):
	template_name = 'home_page.html'

	def get(self, request):
		return render(request, self.template_name)

	def post(self, request):
		if request.FILES['file']:
			uploaded_file = request.FILES['file']
			name, extension = os.path.splitext(uploaded_file.name)

			if uploaded_file.size <= settings.MAX_FILE_SIZE:

				upload_hash = get_random_string(length=random.randint(3, 12))
				loc = settings.FILES_ROOT+'/'+upload_hash+extension.lower()
				with open(loc, 'wb+') as destination:
					for chunk in uploaded_file.chunks():
						destination.write(chunk)

				checksums = get_checksums(loc)

				web_path = settings.FILES_URL.replace('/', '', 1)+upload_hash+extension.lower()

				return JsonResponse({"status": 200, "msg": "Ok", "key": web_path, "url": "https://"+settings.MY_HOST_DOMAIN+"/"+web_path, "checksums": checksums})
			else:
				return JsonResponse({"status": 403, "msg": "File size is too large. Max size is " +
					str(size(settings.MAX_FILE_SIZE, system=alternative)), "key": False, "url": False, "checksums": False})
		else:
			return JsonResponse({"status": 403, "msg": "File was not set in the POST params.", "key": False, "url": False, "checksums": False})
