from decorator_include import decorator_include
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from blamo import auth

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth.auth_login, name='login'),
    url(r'^logout/$', auth.auth_logout, name='logout'),
    url(r'^$', auth.index, name='index'),

    url(r'^blamo/api/', include('blamo.api')),
    url(r'^blamo/', decorator_include(login_required, 'blamo.urls')),
]
