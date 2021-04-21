# config/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  # Django admin
                  path('cae2f32842405201a98951f972e8339310c7555b96ff96a40fb7f49fa534ff1f/', admin.site.urls),

                  # User management
                  path('accounts/', include('allauth.urls')),

                  # Local apps
                  path('', include('pages.urls')),
                  path('books/', include('books.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
