# Generated by Django 3.0.3 on 2020-04-19 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0028_auto_20200418_1320'),
    ]

    operations = [
        migrations.CreateModel(
            name='venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue_name', models.CharField(blank=True, choices=[('L-1', 'L-1'), ('L-2', 'L-2'), ('L-3', 'L-3'), ('L-4', 'L-4'), ('L-5', 'L-5'), ('L-6', 'L-6'), ('L-7', 'L-7'), ('L-8', 'L-8'), ('L-9', 'L-9'), ('L-10', 'L-10'), ('L-11', 'L-11'), ('L-12', 'L-12'), ('L-13', 'L-13'), ('L-14', 'L-14'), ('L-15', 'L-15'), ('L-16', 'L-16'), ('L-17', 'L-17'), ('L-18', 'L-18'), ('L-19', 'L-19'), ('L-20', 'L-20'), ('L-21', 'L-21'), ('L-22', 'L-22'), ('L-23', 'L-23'), ('L-24', 'L-24'), ('L-25', 'L-25'), ('L-26', 'L-26'), ('L-27', 'L-27'), ('L-28', 'L-28'), ('L-29', 'L-29'), ('L-30', 'L-30'), ('L-31', 'L-31'), ('LAB-1', 'LAB-1'), ('LAB-2', 'LAB-2'), ('LAB-3', 'LAB-3'), ('Auditorium', 'Auditorium')], default=None, max_length=50, null=True)),
                ('is_booked', models.BooleanField(blank=True, default=None, null=True)),
                ('date_from', models.DateField(blank=True, default=None, null=True)),
                ('date_to', models.DateField(blank=True, default=None, null=True)),
                ('time_from', models.TimeField(blank=True, default=None, null=True)),
                ('time_to', models.TimeField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='auditorium',
            name='reason_for_disapproval',
            field=models.TextField(blank=True, default=None, help_text='Only required, if you are going to disapprove the application', null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='reason_for_disapproval',
            field=models.TextField(blank=True, default=None, help_text='Only required, if you are going to disapprove the application', null=True),
        ),
        migrations.AddField(
            model_name='labs',
            name='reason_for_disapproval',
            field=models.TextField(blank=True, default=None, help_text='Only required, if you are going to disapprove the application', null=True),
        ),
        migrations.AddField(
            model_name='reimbursement',
            name='reason_for_disapproval',
            field=models.TextField(blank=True, default=None, help_text='Only required, if you are going to disapprove the application', null=True),
        ),
        migrations.AlterField(
            model_name='labs',
            name='full_name',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lecturehalls',
            name='reason_for_disapproval',
            field=models.TextField(blank=True, default=None, help_text='Only required, if you are going to disapprove the application', null=True),
        ),
    ]