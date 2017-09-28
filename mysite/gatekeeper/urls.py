from django.conf.urls import url

from . import views

app_name = 'gatekeeper'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<sugestion_id>[0-9]+)/$', views.sugestions, name='sugestion'),
	url(r'^add_sugestion/$', views.add_sugestion, name='add_sugestion'),
	url(r'^sign_in/$', views.sign_in, name='sign_in'),
]
