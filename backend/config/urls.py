from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('backend.api.urls')),
    path('auth/', include('backend.authentication.urls')),
    path('tasks/', include('backend.tasks.urls')),
]
