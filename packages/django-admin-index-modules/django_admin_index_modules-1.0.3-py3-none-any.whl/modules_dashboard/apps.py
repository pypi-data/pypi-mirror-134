from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig
from django.utils.translation import gettext_lazy as _

class CustomAdminConfig(AdminConfig):
    default_site = 'modules_dashboard.admin.CustomAdminSite'


class ModulesDashboardsConfig(AppConfig):
    default_auto_field = 'modules_dashboard.db.models.BigAutoField'
    name = 'Dashboard'
