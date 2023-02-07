from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductCreateAPIView.as_view(), name='api-create-view'),
    path('list-create/', views.ProductListCreateAPIView.as_view(), name='api-list-create-view'),
    path('list/', views.ProductListAPIView.as_view(), name='api-list-view'),
    path('<int:pk>/', views.ProductDetailAPIView.as_view(), name='api-detail-view'),
    path('<int:pk>/delete/', views.ProductDeleteAPIView.as_view(), name='api-delete-view'),
    path('<int:pk>/update/', views.ProductUpdateAPIView.as_view(), name='api-update-view'),
    path('func/<int:pk>/', views.product_alt_view, name='detail-alt-view'), #function based alt view as detail view
    path('func/list/', views.product_alt_view, name='list-alt-view'), #function based alt view as list view
    path('func/create/', views.product_alt_view, name='create-alt-view'),#function based alt view as create view
    path('search/', views.SearchListView.as_view(), name='api-search-view'),
    path('algolia-search/', views.AlgoliaSearchListView.as_view(), name='api-search-view'),
]