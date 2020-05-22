from django.urls import path

from . import views

urlpatterns = [
    # diffrent endpoints paths...    
    path('user/', views.UserCreate.as_view(), name='user-create'),
    path('user/<int:pk>/', views.UserUpdate.as_view(), name='user-update'),
    path('client/', views.ClientCreate.as_view(), name='client-create'),
    path('client/<int:pk>/', views.ClientUpdate.as_view(), name='client-update')
    # diffrent endpoints paths...
]