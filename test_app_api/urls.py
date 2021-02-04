from django.urls import path

from . import views

urlpatterns = [
    path('merchants/', views.MerchantListView.as_view()),
    path('merchants/<int:pk>', views.MerchantDetailView.as_view()),
    path('products/', views.ProductListView.as_view()),
    path('products/<int:pk>', views.ProductDetailView.as_view()),
]