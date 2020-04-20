from django.db import models
from django.contrib.auth.models import AbstractUser

from core.custom.model_fields import LowerCharField


class CustomUser(AbstractUser):
    profile_picture = models.ImageField(
        "Profile picture", upload_to="profile/%Y/%m/%d"
    )
    birthday = models.DateField("Birthday", blank=True, null=True)
    twitter = LowerCharField("Twitter Account", blank=True, null=True)
    linkedin = LowerCharField("LinkedIn Account", blank=True, null=True)
