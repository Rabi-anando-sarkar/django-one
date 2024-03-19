from django.contrib import admin
from django.urls import path,include
from home.views import home_page

urlpatterns = [
    path("", home_page),
    path("api/v1/",include('api.urls')),
    path('admin/', admin.site.urls),
]
