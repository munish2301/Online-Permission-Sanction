# Generated by Django 3.0.3 on 2020-03-30 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_reimbursementmodel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='reimbursementModel',
            new_name='reimbursement',
        ),
    ]
