from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogView.as_view(), name='list'),
    path('create/', views.BlogCreate.as_view(), name='new'),
    path('detail/<int:pk>/', views.BlogDetail.as_view(), name='detail'),
    path('update/<int:pk>/', views.BlogUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', views.BlogDelete.as_view(), name='delete'),
]