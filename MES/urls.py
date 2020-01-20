
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('Views.urls')),
    # url(r'^admin/', admin.site.urls),
    # path('admin/', admin.site.urls),
]