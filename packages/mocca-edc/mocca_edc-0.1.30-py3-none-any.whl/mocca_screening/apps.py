from django.apps import AppConfig as DjangoApponfig


class AppConfig(DjangoApponfig):
    name = "mocca_screening"
    verbose_name = "MOCCA: Screening"
    screening_age_adult_upper = 99
    screening_age_adult_lower = 18
    include_in_administration_section = True
    has_exportable_data = True
