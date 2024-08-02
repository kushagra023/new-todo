from django.http import HttpResponse
from django_prometheus.exports import ExportToPrometheus
from django.views import View

class MetricsView(View):
    content_type = 'text/plain; charset=utf-8'

    def get(self, request, *args, **kwargs):
        # Generate Prometheus metrics content
        content = ExportToPrometheus().get_metrics()
        return HttpResponse(content, content_type=self.content_type)
