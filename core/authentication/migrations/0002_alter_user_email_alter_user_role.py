# Generated by Django 5.1.6 on 2025-02-20 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('usuario', 'Usuário'), ('personal', 'Personal')], max_length=10),
        ),
    ]
