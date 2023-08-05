from django.test import TestCase, override_settings
from edc_auth.auth_updater import AuthUpdater
from edc_auth.site_auths import site_auths


class TestAuths(TestCase):
    @override_settings(
        EDC_AUTH_SKIP_SITE_AUTHS=False,
        EDC_AUTH_SKIP_AUTH_UPDATER=True,
    )
    def test_load(self):
        site_auths.autodiscover()
        AuthUpdater(verbose=False)
