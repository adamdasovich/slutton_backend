from django.urls import path, include, re_path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('products', views.products, name='products'),
    path('product_detail/<slug:slug>', views.product_detail, name='product_detail'),
    path('add_item', views.add_item, name='add_item'),
    path('product_in_cart', views.product_in_cart, name='product_in_cart'),
    path('get_cart_stat', views.get_cart_stat, name='get_cart_stat'),
    path('get_cart', views.get_cart, name='get_cart'),
    path('update_quantity', views.update_quantity, name='update_quantity'),
    path('delete_cartitem', views.delete_cartitem, name='delete_cartitem'),
    path('get_username', views.get_username, name='get_username'),
    path('user_info', views.user_info, name='user_info'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register', views.UserRegistrationView.as_view(), name='register'),
    path('initiate_paypal_payment/', views.initiate_paypal_payment, name='initial_paypal_payment'),
    path('paypal_payment_callback/', views.paypal_payment_callback, name='paypal_payment_callback'),
]
