from django.db import models
from core.models import CoreModel
from core.custom.model_fields import LowerCharField


class Author(CoreModel):
    GENDER = [
        ("F", "Female"),
        ("M", "Male"),
        ("P", "Private"),
    ]
    first_name = LowerCharField("First name", max_length=50)
    last_name = LowerCharField("Last name", max_length=50)
    bio = models.TextField("Biography", null=True, blank=True)
    picture = models.ImageField("Profile picture", upload_to="authors/%Y/%m/%d")
    birthday = models.DateField("Birthday", blank=True, null=True)
    twitter = LowerCharField(
        "Twitter Account", blank=True, null=True, max_length=120
    )
    linkedin = LowerCharField(
        "LinkedIn Account", blank=True, null=True, max_length=120
    )
    gender = models.CharField("Gender", choices=GENDER, max_length=1)

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"
