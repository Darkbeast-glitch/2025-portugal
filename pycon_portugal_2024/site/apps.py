from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SiteConfig(AppConfig):
    name = "pycon_portugal_2024.site"
    verbose_name = _("SitePackage")

    def ready(self):
        pass
