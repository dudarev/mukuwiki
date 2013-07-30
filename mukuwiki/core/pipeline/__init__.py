from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def check_github(request, backend, *args, **kwargs):
    """
    This goes into django-social-auth login pipeline.
    One cannot login with github if he has not logged in with Twitter before.
    """
    if backend.name == 'github' and request.user and not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('login_with_twitter_first'))
