from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig
from django.utils.translation import gettext_lazy as _

class CustomAdminConfig(AdminConfig):
    default_site = 'dashboard.admin.CustomAdminSite'


class DashboardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dashboard'
