# Generated by Django 4.1.7 on 2023-04-03 19:44

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0003_candidate_candidate_image_alter_candidate_state"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="candidate",
            name="candidate_image",
        ),
    ]
