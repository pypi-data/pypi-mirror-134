# Generated by Django 3.2.10 on 2021-12-09 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mocca_prn', '0003_auto_20211209_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicallosstofollowup',
            name='ltfu_category',
            field=models.CharField(choices=[('unknown_address', 'Changed to an unknown address'), ('never_returned', 'Did not return despite reminders'), ('bad_contact_details', 'Inaccurate contact details'), ('OTHER', 'Other, please specify ...')], max_length=25, verbose_name='Category of loss to follow up'),
        ),
        migrations.AlterField(
            model_name='losstofollowup',
            name='ltfu_category',
            field=models.CharField(choices=[('unknown_address', 'Changed to an unknown address'), ('never_returned', 'Did not return despite reminders'), ('bad_contact_details', 'Inaccurate contact details'), ('OTHER', 'Other, please specify ...')], max_length=25, verbose_name='Category of loss to follow up'),
        ),
    ]
