# Generated by Django 3.1.8 on 2021-04-27 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mocca_ae', '0003_auto_20210225_0604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deathreport',
            name='narrative',
            field=models.TextField(null=True, verbose_name='Narrative'),
        ),
        migrations.AlterField(
            model_name='historicaldeathreport',
            name='narrative',
            field=models.TextField(null=True, verbose_name='Narrative'),
        ),
    ]
