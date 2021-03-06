# Generated by Django 3.0.3 on 2020-04-16 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0018_lecturehalls_sender_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={},
        ),
        migrations.RemoveField(
            model_name='auditorium',
            name='name_of_club_or_technical_society_or_NSS_or_NCC',
        ),
        migrations.RemoveField(
            model_name='lecturehalls',
            name='sender_id',
        ),
        migrations.AddField(
            model_name='auditorium',
            name='CDGC_approval',
            field=models.CharField(choices=[('approved', 'approved'), ('not approved', 'not approved')], default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='auditorium',
            name='DA_approval',
            field=models.CharField(choices=[('approved', 'approved'), ('not approved', 'not approved')], default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='auditorium',
            name='DSA_approval',
            field=models.CharField(choices=[('approved', 'approved'), ('not approved', 'not approved')], default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='auditorium',
            name='OI_approval',
            field=models.CharField(choices=[('approved', 'approved'), ('not approved', 'not approved')], default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='auditorium',
            name='name_of_club_or_technical_society',
            field=models.CharField(blank=True, choices=[('AMS', 'AMS'), ('ASCE', 'ASCE'), ('ASME', 'ASME'), ('ACM', 'ACM'), ('IIM', 'IIM'), ('ISTE', 'ISTE'), ('IEEE', 'IEEE'), ('IETE', 'IETE'), ('SAE', 'SAE'), ('SME', 'SME'), ('SESI', 'SESI'), ('ROBOTICS', 'ROBOTICS'), ('NSS', 'NSS'), ('NCC', 'NCC'), ('Art and Photography Club', 'Art and Photography Club'), ('Music Club', 'Music Club'), ('Dramatics Club', 'Dramatics Club'), ('Speakers Association & Study Circle', 'Speakers Association & Study Circle'), ('Projection Design Club', 'Projection Design Club'), ('Rotaract Club', 'Rotaract Club'), ('Communication Club', 'Communication Club'), ('Student Counselling Cell', 'Student Counselling Cell'), ('Women Empowerment Cell', 'Women Empowerment Cell'), ('EIC', 'EIC')], default=None, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='auditorium',
            name='type',
            field=models.CharField(blank=True, choices=[('Technical', 'Technical'), ('Cultural', 'Cultural')], default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='CA_approval',
            field=models.CharField(choices=[('approved', 'approved'), ('not approved', 'not approved')], default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='CCS_CTS_approval',
            field=models.CharField(choices=[('approved', 'approved'), ('not approved', 'not approved')], default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='DA_approval',
            field=models.CharField(choices=[('approved', 'approved'), ('not approved', 'not approved')], default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='DSA_approval',
            field=models.CharField(choices=[('approved', 'approved'), ('not approved', 'not approved')], default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='OI_approval',
            field=models.CharField(choices=[('approved', 'approved'), ('not approved', 'not approved')], default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='type',
            field=models.CharField(blank=True, choices=[('Technical', 'Technical'), ('Cultural', 'Cultural')], default=None, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='labs',
            name='DA_approval',
            field=models.CharField(choices=[('approved', 'approved'), ('not approved', 'not approved')], default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='labs',
            name='DSA_approval',
            field=models.CharField(choices=[('approved', 'approved'), ('not approved', 'not approved')], default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='labs',
            name='HOD_approval',
            field=models.CharField(choices=[('approved', 'approved'), ('not approved', 'not approved')], default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='labs',
            name='department_related_to_project',
            field=models.CharField(blank=True, choices=[('Computer Science and Engineering', 'Computer Science and Engineering'), ('Electronics and Communication Engineering', 'Electronics and Communication Engineering'), ('Electrical Engineering', 'Electrical Engineering'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Civil Engineering', 'Civil Engineering'), ('Production and Industrial Engineering', 'Production and Industrial Engineering'), ('Aerospace Engineering', 'Aerospace Engineering'), ('Metallurgical Engineering', 'Metallurgical Engineering')], default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='lecturehalls',
            name='OISecurity_approval',
            field=models.CharField(choices=[('approved', 'approved'), ('not approved', 'not approved')], default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='lecturehalls',
            name='OI_approval',
            field=models.CharField(choices=[('approved', 'approved'), ('not approved', 'not approved')], default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='lecturehalls',
            name='type',
            field=models.CharField(blank=True, choices=[('Technical', 'Technical'), ('Cultural', 'Cultural')], default=None, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='reimbursement',
            name='CA_approval',
            field=models.CharField(choices=[('approved', 'approved'), ('not approved', 'not approved')], default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='reimbursement',
            name='CCS_CTS_approval',
            field=models.CharField(choices=[('approved', 'approved'), ('not approved', 'not approved')], default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='reimbursement',
            name='DA_approval',
            field=models.CharField(choices=[('approved', 'approved'), ('not approved', 'not approved')], default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='reimbursement',
            name='DSA_approval',
            field=models.CharField(choices=[('approved', 'approved'), ('not approved', 'not approved')], default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='reimbursement',
            name='OI_approval',
            field=models.CharField(choices=[('approved', 'approved'), ('not approved', 'not approved')], default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='reimbursement',
            name='Secretary_approval',
            field=models.CharField(choices=[('approved', 'approved'), ('not approved', 'not approved')], default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='reimbursement',
            name='type',
            field=models.CharField(blank=True, choices=[('Technical', 'Technical'), ('Cultural', 'Cultural')], default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='name_of_club_or_technical_society',
            field=models.CharField(blank=True, choices=[('AMS', 'AMS'), ('ASCE', 'ASCE'), ('ASME', 'ASME'), ('ACM', 'ACM'), ('IIM', 'IIM'), ('ISTE', 'ISTE'), ('IEEE', 'IEEE'), ('IETE', 'IETE'), ('SAE', 'SAE'), ('SME', 'SME'), ('SESI', 'SESI'), ('ROBOTICS', 'ROBOTICS'), ('NSS', 'NSS'), ('NCC', 'NCC'), ('Art and Photography Club', 'Art and Photography Club'), ('Music Club', 'Music Club'), ('Dramatics Club', 'Dramatics Club'), ('Speakers Association & Study Circle', 'Speakers Association & Study Circle'), ('Projection Design Club', 'Projection Design Club'), ('Rotaract Club', 'Rotaract Club'), ('Communication Club', 'Communication Club'), ('Student Counselling Cell', 'Student Counselling Cell'), ('Women Empowerment Cell', 'Women Empowerment Cell'), ('EIC', 'EIC')], default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='labs',
            name='branch',
            field=models.CharField(blank=True, choices=[('Computer Science and Engineering', 'Computer Science and Engineering'), ('Electronics and Communication Engineering', 'Electronics and Communication Engineering'), ('Electrical Engineering', 'Electrical Engineering'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Civil Engineering', 'Civil Engineering'), ('Production and Industrial Engineering', 'Production and Industrial Engineering'), ('Aerospace Engineering', 'Aerospace Engineering'), ('Metallurgical Engineering', 'Metallurgical Engineering')], default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='labs',
            name='year',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default=None, max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='lecturehalls',
            name='name_of_club_or_technical_society',
            field=models.CharField(blank=True, choices=[('AMS', 'AMS'), ('ASCE', 'ASCE'), ('ASME', 'ASME'), ('ACM', 'ACM'), ('IIM', 'IIM'), ('ISTE', 'ISTE'), ('IEEE', 'IEEE'), ('IETE', 'IETE'), ('SAE', 'SAE'), ('SME', 'SME'), ('SESI', 'SESI'), ('ROBOTICS', 'ROBOTICS'), ('NSS', 'NSS'), ('NCC', 'NCC'), ('Art and Photography Club', 'Art and Photography Club'), ('Music Club', 'Music Club'), ('Dramatics Club', 'Dramatics Club'), ('Speakers Association & Study Circle', 'Speakers Association & Study Circle'), ('Projection Design Club', 'Projection Design Club'), ('Rotaract Club', 'Rotaract Club'), ('Communication Club', 'Communication Club'), ('Student Counselling Cell', 'Student Counselling Cell'), ('Women Empowerment Cell', 'Women Empowerment Cell'), ('EIC', 'EIC')], default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='reimbursement',
            name='branch',
            field=models.CharField(blank=True, choices=[('Computer Science and Engineering', 'Computer Science and Engineering'), ('Electronics and Communication Engineering', 'Electronics and Communication Engineering'), ('Electrical Engineering', 'Electrical Engineering'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Civil Engineering', 'Civil Engineering'), ('Production and Industrial Engineering', 'Production and Industrial Engineering'), ('Aerospace Engineering', 'Aerospace Engineering'), ('Metallurgical Engineering', 'Metallurgical Engineering')], default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='reimbursement',
            name='name_of_club_or_technical_society',
            field=models.CharField(blank=True, choices=[('AMS', 'AMS'), ('ASCE', 'ASCE'), ('ASME', 'ASME'), ('ACM', 'ACM'), ('IIM', 'IIM'), ('ISTE', 'ISTE'), ('IEEE', 'IEEE'), ('IETE', 'IETE'), ('SAE', 'SAE'), ('SME', 'SME'), ('SESI', 'SESI'), ('ROBOTICS', 'ROBOTICS'), ('NSS', 'NSS'), ('NCC', 'NCC'), ('Art and Photography Club', 'Art and Photography Club'), ('Music Club', 'Music Club'), ('Dramatics Club', 'Dramatics Club'), ('Speakers Association & Study Circle', 'Speakers Association & Study Circle'), ('Projection Design Club', 'Projection Design Club'), ('Rotaract Club', 'Rotaract Club'), ('Communication Club', 'Communication Club'), ('Student Counselling Cell', 'Student Counselling Cell'), ('Women Empowerment Cell', 'Women Empowerment Cell'), ('EIC', 'EIC')], default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='reimbursement',
            name='year',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default=None, max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='branch',
            field=models.CharField(blank=True, choices=[('Computer Science and Engineering', 'Computer Science and Engineering'), ('Electronics and Communication Engineering', 'Electronics and Communication Engineering'), ('Electrical Engineering', 'Electrical Engineering'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Civil Engineering', 'Civil Engineering'), ('Production and Industrial Engineering', 'Production and Industrial Engineering'), ('Aerospace Engineering', 'Aerospace Engineering'), ('Metallurgical Engineering', 'Metallurgical Engineering')], default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='department',
            field=models.CharField(blank=True, choices=[('Computer Science and Engineering', 'Computer Science and Engineering'), ('Electronics and Communication Engineering', 'Electronics and Communication Engineering'), ('Electrical Engineering', 'Electrical Engineering'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Civil Engineering', 'Civil Engineering'), ('Production and Industrial Engineering', 'Production and Industrial Engineering'), ('Aerospace Engineering', 'Aerospace Engineering'), ('Metallurgical Engineering', 'Metallurgical Engineering')], default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='society_or_club_name',
            field=models.CharField(blank=True, choices=[('AMS', 'AMS'), ('ASCE', 'ASCE'), ('ASME', 'ASME'), ('ACM', 'ACM'), ('IIM', 'IIM'), ('ISTE', 'ISTE'), ('IEEE', 'IEEE'), ('IETE', 'IETE'), ('SAE', 'SAE'), ('SME', 'SME'), ('SESI', 'SESI'), ('ROBOTICS', 'ROBOTICS'), ('NSS', 'NSS'), ('NCC', 'NCC'), ('Art and Photography Club', 'Art and Photography Club'), ('Music Club', 'Music Club'), ('Dramatics Club', 'Dramatics Club'), ('Speakers Association & Study Circle', 'Speakers Association & Study Circle'), ('Projection Design Club', 'Projection Design Club'), ('Rotaract Club', 'Rotaract Club'), ('Communication Club', 'Communication Club'), ('Student Counselling Cell', 'Student Counselling Cell'), ('Women Empowerment Cell', 'Women Empowerment Cell'), ('EIC', 'EIC')], default=None, max_length=50, null=True),
        ),
    ]
