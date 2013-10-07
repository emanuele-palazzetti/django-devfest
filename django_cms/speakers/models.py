from django.db import models
from django.utils.translation import ugettext as _

from cms.models.pluginmodel import CMSPlugin


class Speaker(CMSPlugin):
    first_name = models.CharField(_("First name"), max_length=50)
    last_name = models.CharField(_("Last name"), max_length=50)
    email = models.EmailField(_("Email"), null=True, blank=True)
    assignment = models.CharField(_("Company assignment"), max_length=200, null=True, blank=True)
    bio = models.TextField(_("Biography"), max_length=2000, null=True, blank=True)

    # Social links
    social_website = models.URLField(_("Website"), null=True, blank=True)
    social_google = models.URLField(_("Google+"), null=True, blank=True)
    social_twitter = models.URLField(_("Twitter"), null=True, blank=True)
    social_linkedin = models.URLField(_("Linkedin"), null=True, blank=True)
    social_github = models.URLField(_("Github"), null=True, blank=True)

    @property
    def full_name(self):
        return u'{0} {1}'.format(self.first_name, self.last_name)

    # Django CMS 3 beta2 doesn't support Python 3
    def __unicode__(self):
        return self.full_name
