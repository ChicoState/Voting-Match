# Generated by Django 3.2.17 on 2023-02-21 23:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_voter'),
    ]

    operations = [
        migrations.CreateModel(
            name='CandidateOpinion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.FloatField()),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.candidate')),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('candidate_opinion', models.ManyToManyField(through='core.CandidateOpinion', to='core.Candidate')),
            ],
        ),
        migrations.CreateModel(
            name='UserOpinion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField()),
                ('weight', models.FloatField()),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.issue')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.voter')),
            ],
        ),
        migrations.AddField(
            model_name='issue',
            name='user_opinion',
            field=models.ManyToManyField(through='core.UserOpinion', to='core.Voter'),
        ),
        migrations.AddField(
            model_name='candidateopinion',
            name='issue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.issue'),
        ),
    ]
