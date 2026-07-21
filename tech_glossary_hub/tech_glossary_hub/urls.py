"""
URL configuration for Tech Glossary Hub.

Routes:
- Admin Panel
- Main Application
- REST API
- Custom Error Pages
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

# ==========================================================
# URL PATTERNS
# ==========================================================

urlpatterns = [

    # Django Admin

    path(
        "admin/",
        admin.site.urls,
    ),

    # Main Application

    path(
        "",
        include("glossary.urls"),
    ),

    # REST API

    path(
        "api/",
        include("glossary.api_urls"),
    ),

]


# ==========================================================
# MEDIA FILES (Development Only)
# ==========================================================

if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
    
# ==========================================================
# CUSTOM ERROR HANDLERS
# ==========================================================

handler404 = "glossary.views.custom_404"
handler500 = "glossary.views.custom_500"