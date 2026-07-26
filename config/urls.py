from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),

    # Accounts (Home, Login, Register, Profile)
    path("", include("accounts.urls")),

    # Job Tracker
    path("tracker/", include("tracker.urls")),

    # Resume
    path("resume/", include("resume.urls")),
    
    #hr
    path("hr/", include("hr.urls")),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)