from django.db import models


class UpperTextField(models.TextField):
    def to_python(self, value):
        lower_value = super().to_python(value)
        if lower_value:
            return lower_value.upper()
        return lower_value


class LowerCharField(models.CharField):
    def to_python(self, value):
        lower_value = super().to_python(value)
        if lower_value:
            return lower_value.lower()
        return lower_value


class TitleCharField(models.CharField):
    def to_python(self, value):
        lower_value = super().to_python(value)
        if lower_value:
            return lower_value.title()
        return lower_value


class UpperCharField(models.CharField):
    def to_python(self, value):
        lower_value = super().to_python(value)
        if lower_value:
            return lower_value.upper()
        return lower_value
