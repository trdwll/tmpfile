import os, random

from django.http import JsonResponse
from django.shortcuts import render
from django.utils.crypto import get_random_string
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.conf import settings

from hurry.filesize import size, alternative

@method_decorator(csrf_exempt, name='dispatch')
class PasteView(View):
	template_name = 'pastes_home.html'

	def get(self, request):
		return render(request, self.template_name)

	def post(self, request):
		if request.POST['paste']:
			paste_content = request.POST.get('paste', '')

			paste_length = len(paste_content.encode('utf8'))
			
			if paste_length <= settings.MAX_PASTE_SIZE:

				upload_hash = get_random_string(length=random.randint(9, 15))
				with open(settings.PASTES_ROOT+'/'+upload_hash+'.txt', 'w') as paste_file:
					paste_file.write(paste_content)

				web_path = settings.PASTES_URL.replace('/', '', 1)+upload_hash+'.txt'

				return JsonResponse({"status": 200, "msg": "Ok", "key": web_path, "url": "https://"+settings.MY_HOST_DOMAIN+"/"+web_path})
			else:
				return JsonResponse({"status": 403, "msg": "Paste size is too large. Max size is " + 
					str(size(settings.MAX_PASTE_SIZE, system=alternative)), "key": False, "url": False})
		else:
			return JsonResponse({"status": 403, "msg": "Paste was not set in the POST params.", "key": False, "url": False})
