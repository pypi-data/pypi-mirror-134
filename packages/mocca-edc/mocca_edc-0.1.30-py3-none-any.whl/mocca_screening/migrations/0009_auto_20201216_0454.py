# Generated by Django 3.0.9 on 2020-12-16 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mocca_screening", "0008_auto_20201216_0417"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalmoccaregister",
            name="screen_now",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")],
                default="No",
                max_length=15,
                verbose_name="Patient is present. Screen now?",
            ),
        ),
        migrations.AddField(
            model_name="moccaregister",
            name="screen_now",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")],
                default="No",
                max_length=15,
                verbose_name="Patient is present. Screen now?",
            ),
        ),
    ]
