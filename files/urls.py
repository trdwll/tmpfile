"""files URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
	1. Import the include() function: from django.conf.urls import url, include
	2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include

from django.views.generic import TemplateView

from . import views

import pastes

handler400 = 'files.views.handler400'
handler403 = 'files.views.handler403'
handler404 = 'files.views.handler404'
handler500 = 'files.views.handler500'


urlpatterns = [
	url(r'^$', views.HomeView.as_view(), name='home'),
	url(r'^page/pastes/?', include('pastes.urls')),
	url(r'^page/faq/?$', TemplateView.as_view(template_name='faq.html'), name='faq'),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.FILES_URL, document_root=settings.FILES_ROOT)
	urlpatterns += static(settings.PASTES_URL, document_root=settings.PASTES_ROOT)