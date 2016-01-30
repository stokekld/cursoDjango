from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^gatos/', views.gato, name='gato'),
	url(r'^saludo/', views.saludo, name='saludo')
]