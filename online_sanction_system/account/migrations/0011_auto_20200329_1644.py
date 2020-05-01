# Generated by Django 3.0.4 on 2020-03-29 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_auto_20200327_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='department',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='society_or_club_name',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default=None, max_length=1, null=True),
        ),
    ]