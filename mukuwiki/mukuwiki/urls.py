from django.conf.urls import patterns, include, url

from core.views import HomeView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    'photoplanet.views',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns(
    '',
    url(r'', include('social_auth.urls')),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout')
)
