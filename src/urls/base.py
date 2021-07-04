from django.contrib import admin
from django.urls import path
from apps.users.urls import urlpatterns as users_urls
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include(users_urls)),
]
