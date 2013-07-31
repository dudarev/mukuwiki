from django.db import models


class LandingPageContact(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    email = models.EmailField(blank=True)

    def __unicode__(self):
        return "Contact from landing page: {}".format(self.email)
