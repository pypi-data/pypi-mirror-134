# Generated by Django 3.2.9 on 2022-01-09 14:17

import _socket
from django.conf import settings
import django.contrib.sites.managers
from django.db import migrations, models
import django.db.models.deletion
import django_audit_fields.fields.hostname_modification_field
import django_audit_fields.fields.userfield
import django_audit_fields.fields.uuid_auto_field
import django_audit_fields.models.audit_model_mixin
import django_revision.revision_field
import edc_model.models.validators.date
import edc_protocol.validators
import edc_utils.date
import edc_visit_tracking.managers
import simple_history.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("sites", "0002_alter_domain_unique"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("mocca_subject", "0026_auto_20220109_1705"),
    ]

    operations = [
        migrations.CreateModel(
            name="GlucoseFollowup",
            fields=[],
            options={
                "verbose_name": "Glucose: Followup",
                "verbose_name_plural": "Glucose: Followup",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("mocca_subject.glucose",),
            managers=[
                ("on_site", django.contrib.sites.managers.CurrentSiteManager()),
                ("objects", edc_visit_tracking.managers.CrfModelManager()),
            ],
        ),
        migrations.AlterModelOptions(
            name="glucose",
            options={
                "default_permissions": ("add", "change", "delete", "view", "export", "import"),
                "get_latest_by": "modified",
                "ordering": ("-modified", "-created"),
                "verbose_name": "Glucose",
                "verbose_name_plural": "Glucose",
            },
        ),
        migrations.AlterModelOptions(
            name="historicalglucose",
            options={
                "get_latest_by": "history_date",
                "ordering": ("-history_date", "-history_id"),
                "verbose_name": "historical Glucose",
            },
        ),
        migrations.RenameField(
            model_name="glucose",
            old_name="glucose",
            new_name="glucose_value",
        ),
        migrations.RenameField(
            model_name="historicalglucose",
            old_name="glucose",
            new_name="glucose_value",
        ),
        migrations.RenameField(
            model_name="historicalglucosebaseline",
            old_name="glucose",
            new_name="glucose_value",
        ),
        migrations.RenameField(
            model_name="glucose",
            old_name="glucose_assay_datetime",
            new_name="assay_datetime",
        ),
        migrations.RenameField(
            model_name="glucose",
            old_name="glucose_requisition",
            new_name="requisition",
        ),
        migrations.RenameField(
            model_name="historicalglucose",
            old_name="glucose_assay_datetime",
            new_name="assay_datetime",
        ),
        migrations.RenameField(
            model_name="historicalglucose",
            old_name="glucose_requisition",
            new_name="requisition",
        ),
        migrations.RenameField(
            model_name="historicalglucosebaseline",
            old_name="glucose_assay_datetime",
            new_name="assay_datetime",
        ),
        migrations.RenameField(
            model_name="historicalglucosebaseline",
            old_name="glucose_requisition",
            new_name="requisition",
        ),
        migrations.AddField(
            model_name="glucose",
            name="glucose_grade",
            field=models.IntegerField(
                blank=True,
                choices=[
                    (0, "Not graded"),
                    (1, "Grade 1"),
                    (2, "Grade 2"),
                    (3, "Grade 3"),
                    (4, "Grade 4"),
                    (5, "Grade 5"),
                ],
                null=True,
                verbose_name="Grade",
            ),
        ),
        migrations.AddField(
            model_name="glucose",
            name="glucose_grade_description",
            field=models.CharField(
                blank=True, max_length=250, null=True, verbose_name="Grade description"
            ),
        ),
        migrations.AddField(
            model_name="historicalglucose",
            name="glucose_grade",
            field=models.IntegerField(
                blank=True,
                choices=[
                    (0, "Not graded"),
                    (1, "Grade 1"),
                    (2, "Grade 2"),
                    (3, "Grade 3"),
                    (4, "Grade 4"),
                    (5, "Grade 5"),
                ],
                null=True,
                verbose_name="Grade",
            ),
        ),
        migrations.AddField(
            model_name="historicalglucose",
            name="glucose_grade_description",
            field=models.CharField(
                blank=True, max_length=250, null=True, verbose_name="Grade description"
            ),
        ),
        migrations.AddField(
            model_name="historicalglucosebaseline",
            name="glucose_grade",
            field=models.IntegerField(
                blank=True,
                choices=[
                    (0, "Not graded"),
                    (1, "Grade 1"),
                    (2, "Grade 2"),
                    (3, "Grade 3"),
                    (4, "Grade 4"),
                    (5, "Grade 5"),
                ],
                null=True,
                verbose_name="Grade",
            ),
        ),
        migrations.AddField(
            model_name="historicalglucosebaseline",
            name="glucose_grade_description",
            field=models.CharField(
                blank=True, max_length=250, null=True, verbose_name="Grade description"
            ),
        ),
        migrations.AlterField(
            model_name="glucose",
            name="fasting",
            field=models.CharField(
                choices=[("fasting", "Fasting"), ("non_fasting", "Non-fasting")],
                max_length=25,
                null=True,
                verbose_name="Was this fasting or non-fasting?",
            ),
        ),
        migrations.AlterField(
            model_name="glucose",
            name="glucose_quantifier",
            field=models.CharField(
                blank=True,
                choices=[("=", "="), (">", ">"), (">=", ">="), ("<", "<"), ("<=", "<=")],
                default="=",
                max_length=10,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="glucose",
            name="glucose_units",
            field=models.CharField(
                blank=True,
                choices=[("mg/dL", "mg/dL"), ("mmol/L", "mmol/L (millimoles/L)")],
                max_length=15,
                null=True,
                verbose_name="units",
            ),
        ),
        migrations.AlterField(
            model_name="historicalglucose",
            name="fasting",
            field=models.CharField(
                choices=[("fasting", "Fasting"), ("non_fasting", "Non-fasting")],
                max_length=25,
                null=True,
                verbose_name="Was this fasting or non-fasting?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalglucose",
            name="glucose_quantifier",
            field=models.CharField(
                blank=True,
                choices=[("=", "="), (">", ">"), (">=", ">="), ("<", "<"), ("<=", "<=")],
                default="=",
                max_length=10,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="historicalglucose",
            name="glucose_units",
            field=models.CharField(
                blank=True,
                choices=[("mg/dL", "mg/dL"), ("mmol/L", "mmol/L (millimoles/L)")],
                max_length=15,
                null=True,
                verbose_name="units",
            ),
        ),
        migrations.AlterField(
            model_name="historicalglucosebaseline",
            name="fasting",
            field=models.CharField(
                choices=[("fasting", "Fasting"), ("non_fasting", "Non-fasting")],
                max_length=25,
                null=True,
                verbose_name="Was this fasting or non-fasting?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalglucosebaseline",
            name="glucose_quantifier",
            field=models.CharField(
                blank=True,
                choices=[("=", "="), (">", ">"), (">=", ">="), ("<", "<"), ("<=", "<=")],
                default="=",
                max_length=10,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="historicalglucosebaseline",
            name="glucose_units",
            field=models.CharField(
                blank=True,
                choices=[("mg/dL", "mg/dL"), ("mmol/L", "mmol/L (millimoles/L)")],
                max_length=15,
                null=True,
                verbose_name="units",
            ),
        ),
        migrations.CreateModel(
            name="HistoricalGlucoseFollowup",
            fields=[
                (
                    "revision",
                    django_revision.revision_field.RevisionField(
                        blank=True,
                        editable=False,
                        help_text="System field. Git repository tag:branch:commit.",
                        max_length=75,
                        null=True,
                        verbose_name="Revision",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
                    ),
                ),
                (
                    "modified",
                    models.DateTimeField(
                        blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
                    ),
                ),
                (
                    "user_created",
                    django_audit_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user created",
                    ),
                ),
                (
                    "user_modified",
                    django_audit_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user modified",
                    ),
                ),
                (
                    "hostname_created",
                    models.CharField(
                        blank=True,
                        default=_socket.gethostname,
                        help_text="System field. (modified on create only)",
                        max_length=60,
                    ),
                ),
                (
                    "hostname_modified",
                    django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                        blank=True,
                        help_text="System field. (modified on every save)",
                        max_length=50,
                    ),
                ),
                ("device_created", models.CharField(blank=True, max_length=10)),
                ("device_modified", models.CharField(blank=True, max_length=10)),
                (
                    "id",
                    django_audit_fields.fields.uuid_auto_field.UUIDAutoField(
                        blank=True,
                        db_index=True,
                        editable=False,
                        help_text="System auto field. UUID primary key.",
                    ),
                ),
                (
                    "report_datetime",
                    models.DateTimeField(
                        default=edc_utils.date.get_utcnow,
                        help_text="If reporting today, use today's date/time, otherwise use the date/time this information was reported.",
                        validators=[
                            edc_protocol.validators.datetime_not_before_study_start,
                            edc_model.models.validators.date.datetime_not_future,
                        ],
                        verbose_name="Report Date",
                    ),
                ),
                ("consent_model", models.CharField(editable=False, max_length=50, null=True)),
                (
                    "consent_version",
                    models.CharField(editable=False, max_length=10, null=True),
                ),
                (
                    "history_id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False
                    ),
                ),
                (
                    "crf_status",
                    models.CharField(
                        choices=[
                            ("INCOMPLETE", "Incomplete (some data pending)"),
                            ("COMPLETE", "Complete"),
                        ],
                        default="INCOMPLETE",
                        help_text="If some data is still pending, flag this CRF as incomplete",
                        max_length=25,
                        verbose_name="CRF status",
                    ),
                ),
                (
                    "crf_status_comments",
                    models.TextField(
                        blank=True,
                        help_text="for example, why some data is still pending",
                        null=True,
                        verbose_name="Any comments related to status of this CRF",
                    ),
                ),
                (
                    "glucose_units",
                    models.CharField(
                        blank=True,
                        choices=[("mg/dL", "mg/dL"), ("mmol/L", "mmol/L (millimoles/L)")],
                        max_length=15,
                        null=True,
                        verbose_name="units",
                    ),
                ),
                (
                    "glucose_abnormal",
                    models.CharField(
                        blank=True,
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=25,
                        null=True,
                        verbose_name="abnormal",
                    ),
                ),
                (
                    "glucose_reportable",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("N/A", "Not applicable"),
                            ("3", "Yes, grade 3"),
                            ("4", "Yes, grade 4"),
                            ("No", "Not reportable"),
                            ("Already reported", "Already reported"),
                            ("present_at_baseline", "Present at baseline"),
                        ],
                        max_length=25,
                        null=True,
                        verbose_name="reportable",
                    ),
                ),
                (
                    "glucose_grade",
                    models.IntegerField(
                        blank=True,
                        choices=[
                            (0, "Not graded"),
                            (1, "Grade 1"),
                            (2, "Grade 2"),
                            (3, "Grade 3"),
                            (4, "Grade 4"),
                            (5, "Grade 5"),
                        ],
                        null=True,
                        verbose_name="Grade",
                    ),
                ),
                (
                    "glucose_grade_description",
                    models.CharField(
                        blank=True, max_length=250, null=True, verbose_name="Grade description"
                    ),
                ),
                (
                    "is_poc",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=15,
                        null=True,
                        verbose_name="Was a point-of-care test used?",
                    ),
                ),
                (
                    "fasting",
                    models.CharField(
                        choices=[("fasting", "Fasting"), ("non_fasting", "Non-fasting")],
                        max_length=25,
                        null=True,
                        verbose_name="Was this fasting or non-fasting?",
                    ),
                ),
                (
                    "glucose_performed",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=15,
                        verbose_name="Has the patient had their glucose measured today or since the last visit?",
                    ),
                ),
                (
                    "glucose_date",
                    models.DateField(
                        blank=True,
                        null=True,
                        validators=[edc_model.models.validators.date.date_not_future],
                    ),
                ),
                (
                    "glucose_fasted",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No"), ("N/A", "Not applicable")],
                        default="N/A",
                        max_length=15,
                        verbose_name="Has the participant fasted?",
                    ),
                ),
                (
                    "glucose_value",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=8,
                        null=True,
                        verbose_name="Glucose result",
                    ),
                ),
                (
                    "glucose_quantifier",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("=", "="),
                            (">", ">"),
                            (">=", ">="),
                            ("<", "<"),
                            ("<=", "<="),
                        ],
                        default="=",
                        max_length=10,
                        null=True,
                    ),
                ),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "site",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="sites.site",
                    ),
                ),
                (
                    "subject_visit",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="mocca_subject.subjectvisit",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical Glucose: Followup",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
