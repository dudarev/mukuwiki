from django.views.generic import TemplateView
from django import forms
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages

from landing.models import LandingPageContact


class LandingPageContactForm(forms.ModelForm):
    class Meta:
        model = LandingPageContact


class HomeView(CreateView):
    model = LandingPageContact
    form_class = LandingPageContactForm
    template_name = 'mukuwiki/index.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.INFO,
            "Thank you! We'll stay in touch.")
        form.instance.user = self.request.user
        return super(HomeView, self).form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        """
        Adds `is_github_associated` variable to template.
        """

        is_github_associated = False
        if request.user and request.user.is_authenticated():
            associated_users_list = request.user.social_auth.all()
            for u in associated_users_list:
                if u.provider == 'github':
                    is_github_associated = True
                    break
        return super(HomeView, self).dispatch(
            request,
            is_github_associated=is_github_associated,
            *args,
            **kwargs)

        
class LoginWithTwitterFirstView(TemplateView):
    template_name = 'mukuwiki/login_with_twitter_first.html'
