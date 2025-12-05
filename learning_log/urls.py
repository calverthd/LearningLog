from django.contrib import admin
from django.urls import path, include  # ← include is required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('logs.urls')),  # ← Connects your app’s URLs
]

