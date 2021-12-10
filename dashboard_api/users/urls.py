from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import users_api_view
from .views import user_detail_api_view
from .views import user_detail_get
from .views import Test_api_view

urlpatterns = [
    path('users/', users_api_view, name='usuarios_api'),
    path('users/<int:pk>', user_detail_api_view, name='users_detail'),
    path('user/<str:email>', user_detail_get),
    path('users/tests', Test_api_view),
    path('login/', obtain_auth_token),
]
