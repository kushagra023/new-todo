from django.http import HttpResponse
from django_prometheus.exports import ExportToPrometheus

class MetricsView(HttpResponse):
    content_type = 'text/plain; charset=utf-8'
    def __init__(self, *args, **kwargs):
        content = ExportToPrometheus()  # Use the Prometheus exporter
        super().__init__(content, *args, **kwargs)
