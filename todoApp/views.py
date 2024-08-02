from django.http import HttpResponse
from django_prometheus.exports import PrometheusMetrics
from django.views import View

class MetricsView(View):
    content_type = 'text/plain; charset=utf-8'

    def get(self, request, *args, **kwargs):
        metrics = PrometheusMetrics().generate_latest()
        return HttpResponse(metrics, content_type=self.content_type)
