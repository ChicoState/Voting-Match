# Generated by Django 3.2.17 on 2023-02-27 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_candidatescore'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserOpinion',
            new_name='VoterOpinion',
        ),
    ]
