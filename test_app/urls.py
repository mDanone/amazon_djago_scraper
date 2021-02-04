from django.urls import path

from .views import MecrhantsListView

urlpatterns = [
    path('merchants/', MecrhantsListView.as_view())
]
