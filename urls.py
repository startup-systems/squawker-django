from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^squawker/', include('squawker.urls')),
    url(r'^admin/', admin.site.urls),
]
