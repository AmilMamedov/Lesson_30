from django.urls import path
from rest_framework_simplejwt import TokenObtainPairView, TokenRefreshView
from users.views import *
urlpatterns = [
    path('', UserListView.as_view()),
    path('<int:pk>', UserDitailView.as_view()),
    path('create/', UserCreateView.as_view()),
    path('<int:pk>/update/', UserUpdateView.as_view()),
    path('<int:pk>/delete/', UserDeleteView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh', TokenRefreshView.as_view()),

]