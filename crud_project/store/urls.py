from django.urls import path
from .views import StoreListCreateView, StoreDetailView

urlpatterns = [
    path('stores/', StoreListCreateView.as_view(), name='store-list-create'),
    path('stores/<int:pk>/', StoreDetailView.as_view(), name='store-detail'),
]
