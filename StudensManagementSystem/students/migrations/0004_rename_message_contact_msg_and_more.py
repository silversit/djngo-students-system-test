# Generated by Django 5.0.6 on 2024-06-29 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0003_contact"),
    ]

    operations = [
        migrations.RenameField(
            model_name="contact",
            old_name="message",
            new_name="msg",
        ),
        migrations.RenameField(
            model_name="contact",
            old_name="name",
            new_name="subject",
        ),
    ]
