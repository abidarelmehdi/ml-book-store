from django.db import models
from django.contrib.auth.models import AbstractUser

from core.custom.model_fields import LowerCharField


class CustomUser(AbstractUser):
    GENDER = [
        ("F", "Female"),
        ("M", "Male"),
        ("P", "Private"),
    ]
    profile_picture = models.ImageField(
        "Profile picture", upload_to="profile/%Y/%m/%d"
    )
    birthday = models.DateField("Birthday", blank=True, null=True)
    twitter = LowerCharField(
        "Twitter Account", blank=True, null=True, max_length=120
    )
    linkedin = LowerCharField(
        "LinkedIn Account", blank=True, null=True, max_length=120
    )
    gender = models.CharField("Gender", choices=GENDER, max_length=1)

    class Meta:
        indexes = [models.Index(fields=["id"])]
