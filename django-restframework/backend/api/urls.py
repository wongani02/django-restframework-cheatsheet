from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from products.views import ProductListCreateAPIView

urlpatterns = [
    path('', views.api_home, name='api-home'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('blog-list/', views.BlogListCreateAPIView.as_view(), name='blog-list'),
    path('products/', ProductListCreateAPIView.as_view(), name='product-list'),
    path('blog/<int:pk>/', views.BlogDetailAPIView.as_view(), name='blog-detail-view'),
    path('auth/', obtain_auth_token, name='obtain-auth-token'),
]