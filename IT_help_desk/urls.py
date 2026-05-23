from django.contrib import admin
from django.urls import path
import tickets.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('create/', views.create_ticket),
    path('close/<int:id>/', views.close_ticket),
    path('ticket/<int:id>/', views.ticket_detail),
    path('health/', views.health),
]