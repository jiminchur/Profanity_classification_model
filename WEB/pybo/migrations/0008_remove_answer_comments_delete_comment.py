# Generated by Django 4.2.9 on 2024-01-26 01:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("pybo", "0007_alter_comment_create_date"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="answer",
            name="comments",
        ),
        migrations.DeleteModel(
            name="Comment",
        ),
    ]
