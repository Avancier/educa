from django.conf.urls import url, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'courses', views.CourseViewSet)


urlpatterns = [
		'''
		url(r'^courses/(?P<pk>\d+)/enroll/$',views.CourseEnrollView.as_view(),name='course_enroll'),
'''
		url(r'^', include(router.urls)),
				

]
