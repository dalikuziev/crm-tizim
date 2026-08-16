from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('olmaxon/', admin.site.urls),
    path('', include('course.urls')),
    path('course/', include('course.urls')),
    path('account/', include('django.contrib.auth.urls')),
]
