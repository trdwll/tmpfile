from django.conf.urls import url
from . import views


app_name = 'pastes'
urlpatterns = [
	url(r'^$', views.PasteView.as_view(), name='paste-home'),
]