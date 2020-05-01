from core.models import CoreModel
from core.custom.model_fields import TitleCharField


class Category(CoreModel):
    label = TitleCharField("Label", max_length=80, unique=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.label
