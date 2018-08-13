class BlamoLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        """log unhandled 500 errors"""
        import json
        import requests
        import sys
        from datetime import datetime
        from django.conf import settings
        from django.views.debug import ExceptionReporter

        reporter = ExceptionReporter(
            request,
            exception.__class__,
            exception.message,
            sys.exc_info()[2]
        )

        log = {
            'host': request.get_host(),
            'path': request.get_full_path(),
            'username': request.user.username,
            'datetime': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'error_type': exception.__class__.__name__,
            'error_message': exception.message,
            'status_code': "500",
            'raw_html': reporter.get_traceback_html(),
        }

        headers = { 'content-type': 'application/json' }
        
        for host in settings.BLAMO_HOSTS:
            url = host + "/blamo/api/v1/logs/"
            requests.post(url, data=json.dumps(log), headers=headers)
        
        return None
