from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.views.generic import TemplateView, View
from accounts.models import User

class DashboardRedirectView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        if request.user.role == User.Role.ADMIN:
            return redirect("admin_dashboard")
        return redirect("student_dashboard")

class StudentDashboardView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = "dashboard/student_dashboard.html"

    def test_func(self):
        return self.request.user.role == User.Role.USER

class AdminDashboardView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = "dashboard/admin_dashboard.html"

    def test_func(self):
        return self.request.user.role == User.Role.ADMIN

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_users"] = User.objects.count()
        context["users"] = User.objects.all()
        return context
