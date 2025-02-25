# Generated by Django 3.0.5 on 2020-05-01 17:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0008_auto_20200501_0046'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRatings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.SmallIntegerField(verbose_name='Rate')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_ratings', to='book.Book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_ratings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='ratings',
            field=models.ManyToManyField(related_name='books', through='book.UserRatings', to=settings.AUTH_USER_MODEL),
        ),
    ]
