# Generated by Django 3.0.9 on 2020-12-06 19:05

import edc_model_fields.fields.other_charfield
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mocca_screening", "0022_auto_20201206_2140"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalsubjectscreening",
            name="willing_to_consent",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No"), ("N/A", "Not applicable")],
                default="N/A",
                max_length=25,
                verbose_name="Is the patient willing to consent to the MOCCA extension trial",
            ),
        ),
        migrations.AddField(
            model_name="subjectscreening",
            name="willing_to_consent",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No"), ("N/A", "Not applicable")],
                default="N/A",
                max_length=25,
                verbose_name="Is the patient willing to consent to the MOCCA extension trial",
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectscreening",
            name="care_comment",
            field=models.TextField(
                blank=True,
                null=True,
                verbose_name="Additional comments relevant to this patient's care",
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectscreening",
            name="icc_not_in_reason",
            field=models.CharField(
                choices=[
                    (
                        "icc_not_available",
                        "ICC not available (or closed) in this facility",
                    ),
                    ("moved", "Moved out of area"),
                    (
                        "dont_want",
                        "Personally chose not to continue with integrated care",
                    ),
                    (
                        "advised_to_vertical",
                        "Healthcare staff asked patient to return to vertical care",
                    ),
                    ("referred_out", "Referred to another facility without an ICC"),
                    ("N/A", "Not applicable"),
                ],
                default="N/A",
                max_length=25,
                verbose_name="If not integrated care, why not?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectscreening",
            name="icc_since_mocca",
            field=models.CharField(
                choices=[
                    ("Yes", "Yes"),
                    ("partially", "Partially"),
                    ("N/A", "Not applicable"),
                ],
                default="N/A",
                max_length=25,
                verbose_name="Has the patient received integrated care `continuously` since the leaving the MOCCA (orig) trial until now?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectscreening",
            name="icc_since_mocca_comment",
            field=edc_model_fields.fields.other_charfield.OtherCharField(
                blank=True,
                max_length=35,
                null=True,
                verbose_name="If PARTIALLY, please explain",
            ),
        ),
        migrations.AlterField(
            model_name="subjectscreening",
            name="care_comment",
            field=models.TextField(
                blank=True,
                null=True,
                verbose_name="Additional comments relevant to this patient's care",
            ),
        ),
        migrations.AlterField(
            model_name="subjectscreening",
            name="icc_not_in_reason",
            field=models.CharField(
                choices=[
                    (
                        "icc_not_available",
                        "ICC not available (or closed) in this facility",
                    ),
                    ("moved", "Moved out of area"),
                    (
                        "dont_want",
                        "Personally chose not to continue with integrated care",
                    ),
                    (
                        "advised_to_vertical",
                        "Healthcare staff asked patient to return to vertical care",
                    ),
                    ("referred_out", "Referred to another facility without an ICC"),
                    ("N/A", "Not applicable"),
                ],
                default="N/A",
                max_length=25,
                verbose_name="If not integrated care, why not?",
            ),
        ),
        migrations.AlterField(
            model_name="subjectscreening",
            name="icc_since_mocca",
            field=models.CharField(
                choices=[
                    ("Yes", "Yes"),
                    ("partially", "Partially"),
                    ("N/A", "Not applicable"),
                ],
                default="N/A",
                max_length=25,
                verbose_name="Has the patient received integrated care `continuously` since the leaving the MOCCA (orig) trial until now?",
            ),
        ),
        migrations.AlterField(
            model_name="subjectscreening",
            name="icc_since_mocca_comment",
            field=edc_model_fields.fields.other_charfield.OtherCharField(
                blank=True,
                max_length=35,
                null=True,
                verbose_name="If PARTIALLY, please explain",
            ),
        ),
    ]
