# Generated by Django 4.1.4 on 2023-02-07 19:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0002_rename_age_author_author1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='commentss',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]