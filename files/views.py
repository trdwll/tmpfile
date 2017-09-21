import os, random
from .utils import get_checksums

from django.http import JsonResponse
from django.shortcuts import render, render_to_response
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
		uploaded_file = request.FILES['file']
		if uploaded_file:

			# get the file name and extension
			name, extension = os.path.splitext(uploaded_file.name)

			# if the file size is <= the max size then continue to upload
			if uploaded_file.size <= settings.MAX_FILE_SIZE:

				# generate a 'random' string for the file name
				upload_hash = get_random_string(length=random.randint(3, 12))

				# set the file location with extension and use elsewhere
				loc = settings.FILES_ROOT+'/'+upload_hash+extension.lower()

				# write the file to disk
				with open(loc, 'wb+') as destination:
					for chunk in uploaded_file.chunks():
						destination.write(chunk)

				# get checksums after the file is written to disk
				checksums = get_checksums(loc)

				# create the web path location (domain.com/path/file.zip)
				# this could be done better, but this works for now
				web_path = settings.FILES_URL.replace('/', '', 1)+upload_hash+extension.lower()

				# so if you're here then the file was successfully uploaded
				# then we're going to want to return a JSON string so we can parse
				# that data in jQuery on the client
				return JsonResponse({"status": 200, "msg": "Ok", "key": web_path, "url": "https://"+settings.MY_HOST_DOMAIN+"/"+web_path, "checksums": checksums})
			else:
				return JsonResponse({"status": 403, "msg": "File size is too large. Max size is " +
					str(size(settings.MAX_FILE_SIZE, system=alternative)), "key": False, "url": False, "checksums": False})
		else:
			return JsonResponse({"status": 403, "msg": "File was not set in the POST params.", "key": False, "url": False, "checksums": False})


"""
Error pages
"""
def handler400(request):
	return render_to_response('error_pages/400.html', {}, request, status=400)

def handler403(request):
	return render_to_response('error_pages/403.html', {}, request, status=403)

def handler404(request):
	return render_to_response('error_pages/404.html', {}, request, status=404)

def handler500(request):
	return render_to_response('error_pages/500.html', {}, request, status=500)