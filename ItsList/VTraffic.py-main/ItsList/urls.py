from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from VTraffic import views

urlpatterns = [
	path('admin/',admin.site.urls),
	path('', views.VT, name="first")
]