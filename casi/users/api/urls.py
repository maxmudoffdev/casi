from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from casi.users.api.views import RegisterView, VerifyView, LoginView

app_name = "users"

urlpatterns = [
    path("register/",RegisterView.as_view()),
    path("verify/", VerifyView.as_view()),
    path("login/", LoginView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),  # ← shu yerga

]
