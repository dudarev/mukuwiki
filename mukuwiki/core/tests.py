from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import factory
from django.contrib.auth import get_user_model

from social_auth.db.django_models import UserSocialAuth

User = get_user_model()


class UserFactory(factory.DjangoModelFactory):
    FACTORY_FOR = User
        
    email = 'admin@admin.com'
    username = 'admin'
    password = 'adm1n'
        
    is_superuser = True
    is_staff = True
    is_active = True
    
    @classmethod
    def _prepare(cls, create, **kwargs):
        password = kwargs.pop('password', None)
        user = super(UserFactory, cls)._prepare(create, **kwargs)
        if password:
            user.set_password(password)
            if create:
                user.save()
        return user


class SocialUserFactory(factory.DjangoModelFactory):
    FACTORY_FOR = UserSocialAuth
    user = factory.SubFactory(UserFactory)
    provider = 'twitter'
    uid = '1'
    extra_data = {}


class UserAssociationTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        self.user = UserFactory.create()
        # no Github account is associated initially
        self.twitter_social_user = SocialUserFactory.create(user=self.user, provider='twitter')
        self.association_request_string = 'associate Github account'

    def tearDown(self):
        self.browser.quit()
    
    def test_can_create_new_poll_via_admin_site(self):
        # login as admin
        self.browser.get(self.live_server_url + '/admin/')
        
        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys(self.user.username)
        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('adm1n')
        password_field.send_keys(Keys.ENTER)
        
        # go to home page
        self.browser.get(self.live_server_url)
        body = self.browser.find_element_by_tag_name('body')

        # a text requesting to associate Github is there
        self.assertIn(self.association_request_string, body.text)

        # connect Github, text is not there
        self.github_social_user = SocialUserFactory.create(user=self.user, provider='github')
        self.assertNotIn(self.association_request_string, body.text)
