from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'mukuwiki/index.html'

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
