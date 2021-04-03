from django.urls import path

from api import views

urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('client/<str:id>/details', views.ClientListView.as_view(), name='client_details'),
    path('client/create/', views.ClientCreate.as_view(), name='client_create'),
    path('client/<str:pk>/update/', views.ClientUpdate.as_view(), name='client_update'),
    path('client/<str:pk>/delete/', views.ClientDelete.as_view(), name='client_delete'),
]
