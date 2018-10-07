from decorator_include import decorator_include
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.decorators import login_required
import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', views.auth_login, name='login'),
    url(r'^logout/$', views.auth_logout, name='logout'),
    url(r'^$', views.index, name='index'),

    url(r'^blamo/api/', include('blamo.api')),
    url(r'^blamo/logs/', decorator_include(login_required, 'blamo.urls')),
]
