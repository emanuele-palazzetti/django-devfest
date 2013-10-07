from django.utils.translation import ugettext as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class SpeakersHook(CMSApp):
    name = _("Speakers Apphook")
    urls = ["speakers.urls"]

apphook_pool.register(SpeakersHook)
