from django.contrib import admin
from django.urls import path, include
from users import urls as user_urls
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include((user_urls, "auth"), namespace="auth")),
    path("", TemplateView.as_view(template_name="root.html"), name="site_root")
]
