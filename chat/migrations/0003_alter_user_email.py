# Generated by Django 5.0.6 on 2024-07-04 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_room_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=70),
        ),
    ]