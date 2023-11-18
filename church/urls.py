from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("login/", views.loginUser, name='login'),
    path("logout/", views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('upcoming-events/', views.upcoming_events, name='upcoming_events'),
    path('donation_history/', views.donations, name='donation-history'),
    path('view_messages/', views.messages, name='view_messages'),
    path('users/<int:pk>/update/', views.updateProfile, name='update_profile'),
    path('create-donation/', views.createDonation, name='create-donation'),
    path('upcoming-birthdays/', views.upcoming_birthdays, name='upcoming_birthdays'),
    

]


    

 
