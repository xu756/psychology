# from django.conf.urls import url
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve

from server import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('app/', include('app.urls')),
                  url(r'^media/(?P<path>.*)', serve, {"document_root": settings.MEDIA_ROOT}),
              ]
