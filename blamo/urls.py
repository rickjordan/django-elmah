from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.log_index),
	url(r'^(?P<log_id>\d+)$', views.log_detail),
    url(r'^test$', views.log_test),
]
