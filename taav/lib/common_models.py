from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    creatred_time = models.DateTimeField(_("created time"), auto_now_add=True)
    modified_time = models.DateTimeField(_("Modified time"), auto_now=True)


    class Meta:
        abstract = True