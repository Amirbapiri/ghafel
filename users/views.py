from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    PasswordChangeView as BasePasswordChangeView,
    PasswordResetView as BasePasswordResetView,
    PasswordResetConfirmView as BasePasswordConfirmView,
)
from django.views.generic import TemplateView
from django.contrib.messages import success
from django.urls import reverse_lazy

from django_registration.backends.activation.views import (
    ActivationView as BaseActivationView
)


class AccountPage(LoginRequiredMixin, TemplateView):
    template_name = "user/account.html"


class ActivationView(BaseActivationView):
    success_url = reverse_lazy("auth:login")

    def activate(self, *args, **kwargs):
        user = super().activate(*args, **kwargs)
        success(
            self.request,
            "Your account has been activated."
            " You may now login.",
            fail_silently=True,
        )
        return True


class SuccessMessageMixin:
    success_message = "Success!"

    def form_valid(self, form):
        success(
            self.request,
            self.success_message,
            fail_silently=True
        )
        return super().form_valid(form)


class PasswordChangeView(
    SuccessMessageMixin, BasePasswordChangeView
):
    success_message = "Password changed successfully!"
    success_url = reverse_lazy("auth:account")
    template_name = "user/password_change_form.html"


class PasswordResetView(
    SuccessMessageMixin, BasePasswordResetView
):
    email_template_name = "user/password_reset_email.txt"
    subject_template_name = (
        "user/password_reset_subject.txt"
    )
    success_message = "Password email sent: please check your email"
    success_url = reverse_lazy("auth:login")
    template_name = "user/password_reset_form.html"


class PasswordResetConfirmView(
    SuccessMessageMixin, BasePasswordConfirmView
):
    success_message = "Password reset: Please login with your new password."
    success_url = reverse_lazy("auth:login")
    template_name = "user/password_reset_confirm.html"
