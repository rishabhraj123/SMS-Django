from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('login/', views.login,name='login'),
    path('insert/', views.insert,name='insert'),
    path('update/', views.update,name='update'),
    path('delete/', views.delete,name='delete'),
    path('about/', views.about,name='about'),
    path('service/', views.service,name='service'),
    path('contact/', views.contact,name='contact'),
    path('feedback/', views.feedback,name='feedback'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout,name='logout'),
    path('dashboard/',views.dashboard,name='dashboard'),
]