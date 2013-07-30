"""
These go into django-social-auth login pipeline.
"""

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages

from social_auth.models import UserSocialAuth


def check_logged_in_with_twitter(request, backend, *args, **kwargs):
    """
    One cannot login with Github if he has not logged in with Twitter before.
    """
    if backend.name == 'github' and request.user and not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('login_with_twitter_first'))


def check_before_associating_github(request, backend, uid, *args, **kwargs):
    """
    When associating Github with Twitter, check that it is not associated with another account.

    If it is associated redirect to home page.

    Based on `social_auth.backends.pipeline.social.social_auth_user`.
    """
    if backend.name == 'github':
        social_user = UserSocialAuth.get_social_auth(backend.name, uid)
        if social_user:
            if request.user and social_user.user != request.user:
                messages.add_message(
                    request, messages.ERROR,
                    'This Github user is already associated with another account.')
                return HttpResponseRedirect(reverse('home'))
