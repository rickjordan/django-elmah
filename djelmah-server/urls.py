from decorator_include import decorator_include
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from djelmah import auth
import re

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth.auth_login, name='login'),
    url(r'^logout/$', auth.auth_logout, name='logout'),
    url(r'^$', auth.index, name='index'),

    url(r'^djelmah/api/', include('djelmah.api')),
    url(r'^djelmah/', decorator_include(login_required, 'djelmah.urls')),
]

# allow django runserver to serve static files in production mode during testing 
if not settings.DEBUG and not settings.DJELMAH_INCLUDE_BUNDLE:
    from django.views.static import serve

    urlpatterns += [
        url(r'^%s(?P<path>.*)$' % re.escape(settings.STATIC_URL.lstrip('/')), serve, { "document_root": settings.STATIC_ROOT })
    ]
