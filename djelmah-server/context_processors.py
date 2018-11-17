from django.conf import settings

def include_bundle(request):
    return { 'DJELMAH_INCLUDE_BUNDLE': settings.DJELMAH_INCLUDE_BUNDLE }
