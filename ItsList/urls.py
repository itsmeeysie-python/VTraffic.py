from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from VTraffic import views


urlpatterns = [
	path('admin/',admin.site.urls),
	path('', views.Main, name="main"),
	path('id/', views.Identification, name='id/'),
	path('chief/', views.Officer,name='chief/'),
	path('pay/', views.Checkout, name="pay/"),
	path('pay/talk/', views.Communicate,name='pay/talk/'),
	


	
	
]
