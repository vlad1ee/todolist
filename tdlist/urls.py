from django.contrib import admin
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', index_page, name='index_page'),
    path('business/<int:pk>/update/', update, name='business_update'),
    path('signup/', signup, name='signup'),
    path('business/<int:pk>/delete/', business_delete, name='business_delete'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('business/create/', index_page, name='business_create'),
    path('business/<int:pk>/', business_detail, name='business_detail'),

] 
