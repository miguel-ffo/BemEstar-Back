# Generated by Django 5.1.6 on 2025-03-01 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_remove_user_phone_user_personal_alter_user_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
