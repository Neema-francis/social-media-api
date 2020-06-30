# Generated by Django 2.2.3 on 2020-06-26 12:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social_media_api', '0003_auto_20200626_0650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storycards',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='story_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
