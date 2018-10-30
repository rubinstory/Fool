from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.plms, name = 'plms'),
        url(r'^$', views.Course, name = 'Course'),
]
