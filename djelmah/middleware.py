class DjelmahLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        """log unhandled 500 errors"""
        import json, requests, sys
        from datetime import datetime
        from django.conf import settings
        from django.core import serializers
        from django.views.debug import ExceptionReporter
        from models import DjelmahHost, DjelmahLog

        reporter = ExceptionReporter(
            request,
            exception.__class__,
            exception.message,
            sys.exc_info()[2]
        )

        log = DjelmahLog(
            host=request.get_host(),
            path=request.get_full_path(),
            username=request.user.username,
            datetime=datetime.now(),
            error_type=exception.__class__.__name__,
            error_message=exception.message,
            status_code="500",
            raw_html=reporter.get_traceback_html()
        )

        data = serializers.serialize('json', log)

        """
        data = json.dumps({
            'host': request.get_host(),
            'path': request.get_full_path(),
            'username': request.user.username,
            'datetime': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'error_type': exception.__class__.__name__,
            'error_message': exception.message,
            'status_code': "500",
            'raw_html': reporter.get_traceback_html()
        })
        """

        headers = { 'Content-Type': "application/json" }
        hosts = DjelmahHost.objects.filter(active=True)

        for host in hosts:
            if host.hostname == "localhost":
                DjelmahLog.save()
                
            else:
                headers['Authorization'] = "ApiKey {}:{}".format(
                    host.username, host.api_key
                )

                url = host.hostname + "/djelmah/api/v1/logs/"
                requests.post(url, data=data, headers=headers)
            
        return None
