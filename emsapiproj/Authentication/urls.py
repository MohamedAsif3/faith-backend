from django.urls import path
# from rest_framework.authtoken import views
from .views import LoginAPIView, SignupAPIView

urlpatterns = [
    path('signup/', SignupAPIView.as_view()),
    path('login/',LoginAPIView.as_view())
]