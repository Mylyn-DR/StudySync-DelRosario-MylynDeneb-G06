from django.urls import path
from .views import AdminDashboardView, DashboardRedirectView, StudentDashboardView

urlpatterns = [
    path("", DashboardRedirectView.as_view(), name="dashboard"),
    path("student/", StudentDashboardView.as_view(), name="student_dashboard"),
    path("admin-panel/", AdminDashboardView.as_view(), name="admin_dashboard"),
]