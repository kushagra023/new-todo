from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import settings, views
from .views import MetricsView  # Import MetricsView

urlpatterns = [
    path('todos/', include('todos.urls')),
    path('admin/', admin.site.urls),
    path('', views.index),
    path('metrics/', MetricsView.as_view(), name='prometheus-metrics'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
