# Generated by Django 5.1.6 on 2025-07-14 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_post_thumbnail"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="created_at",
            field=models.DateField(auto_now_add=True),
        ),
    ]
