# Generated by Django 3.0.5 on 2020-05-01 18:03

import core.custom.model_fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0009_auto_20200501_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=core.custom.model_fields.UpperCharField(max_length=30, unique=True, verbose_name='ISBN'),
        ),
        migrations.AlterField(
            model_name='userratings',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_ratings', to='book.Book', to_field='isbn'),
        ),
    ]
