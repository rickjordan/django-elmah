from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from models import BlamoLog

def test(request):
    raise Exception("It Works!")

def log_index(request):
    logs = BlamoLog.objects.all().order_by('-datetime')
    return render(request, 'logs.html', { 'logs': logs })

def log_detail(request, log_id):
    log = get_object_or_404(BlamoLog, pk=log_id)
    return HttpResponse(log.raw_html)
