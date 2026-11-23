from django.urls import path
<<<<<<< HEAD
from .views import SignUpView
=======
>>>>>>> 3e6c266b6a1ea7323b10a84a55fb40074fbd0936

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
]
