from django.contrib import admin
from django.urls import path, include
from logs import views as log_views   # import your app’s views

urlpatterns = [
    # Admin site
    path('admin/', admin.site.urls),

    # Static pages
    path('', log_views.home, name='home'),          # homepage
    path('about/', log_views.about, name='about'),  # about page
    path('contact/', log_views.contact, name='contact'),  # contact page

    # Logs app (topics, entries, etc.)
    path('logs/', include('logs.urls')),

    # Authentication (login/logout/password reset)
    path('accounts/', include('django.contrib.auth.urls')),
]
