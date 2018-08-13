from django.conf.urls import include, url
from tastypie.api import Api
from . import resources, views

# api resources
api = Api(api_name='v1')
api.register(resources.BlamoLogResource())

urlpatterns = [
    url(r'^logs$', views.log_index),
	url(r'^logs/(?P<log_id>\d+)$', views.log_detail),
    url(r'^test$', views.test),

    # api
    url(r'^api/', include(api.urls)),
]
