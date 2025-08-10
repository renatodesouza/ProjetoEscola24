
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('app.urls')),
    path('accounts/', include('accounts.urls')),
    path('activities/', include('activities.urls')),
    path('courses/', include('courses.urls')),
    path('messaging/', include('messaging.urls')),
    path('silk/', include('silk.urls', namespace='silk')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
