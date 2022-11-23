from django.test import TestCase
from django.contrib.auth.models import User
from app.models import Redirect
from django.core.cache import cache



class RedirectTests(TestCase):  
          
    def setUp(self):
        user = User.objects.create_user('Nahu', 'nahu@gmail.com', '123456')
        user.save()
        self.client = self.client_class()
        self.client.login(username=user.username, password='123456')

        self.redirect1 = Redirect.objects.create(key='Google', url='google.com.ar', active=True)
        self.redirect2 = Redirect.objects.create(key='Amazon', url='amazon.com', active=False)
    
    def test_redirect_view(self):
        path = "/redirect/Google"
        self.assertTrue(cache.has_key('Google'))

        response = self.client.get(path)
        json = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json['url'], self.redirect1.url)
        self.assertEqual(json['key'], self.redirect1.key)
    
    def test_not_redirect_view(self):
        path = "/redirect/Amazon"
        self.assertFalse(cache.has_key('Amazon'))

        response = self.client.get(path)
        self.assertEqual(response.status_code, 400)

    def test_delete(self):
        obj = Redirect.objects.get(key='Google')
        path = "/redirect/" + str(obj.id) + "/"
        response = self.client.get(path)

        self.assertEqual(response.status_code,200)
        self.assertFalse(Redirect.objects.filter(id=obj.id).exists())