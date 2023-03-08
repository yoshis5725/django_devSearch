from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # giving access to the settings.py file -- need to connect to the media_root
from django.conf.urls.static import static  # helps create url for static files


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('projects.urls'))
]

# The settings.MEDIA_URL setting specifies the base URL for serving media files, while settings.MEDIA_ROOT specifies
# the local filesystem path where uploaded media files are stored. By adding the result of static(settings.MEDIA_URL,
# document_root=settings.MEDIA_ROOT) to the urlpatterns list, the Django application is configured to serve media files
# at the specified URL during development.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


