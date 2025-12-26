from django.contrib import admin
from django.urls import path, include
from universitet.views import home_page
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('universitet.urls')),
    path('', home_page)
]