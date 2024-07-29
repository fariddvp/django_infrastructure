from django.db import models
from django.utils.translation import gettext_lazy as _

from lib.common_models import BaseModel

# Create your models here.


class Location(BaseModel):
    title = models.CharField(_("title"))
    points = models.JSONField(_("points"))


    class Meta:
        verbose_name = _("Location")
        verbose_name_plural = _("Locations")


    def __str__(self):
        return self.title