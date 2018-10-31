from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^Course.html/$', views.Course, name = 'Course'),
        url(r'^Course.html/CProgramming.html/$', views.CProgramming, name = 'CProgramming'),
        url(r'^Course.html/CProgramming.html/Notice.html/$', views.Notice, name = 'Notice'),
        url(r'^Course.html/CProgramming.html/Notice.html/Retest.html/$', views.Retest, name = 'Retest'),
        url(r'^Course.html/CProgramming.html/Notice.html/TestList.html/$', views.TestList, name = 'TestList'),
        url(r'^$', views.plms, name = 'plms'),
        url(r'^p1ms.pusan.ac.kr/$', views.plms, name = 'plms'),
]
