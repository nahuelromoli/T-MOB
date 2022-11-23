from django.utils import timezone
from django.test import TestCase
from app.models import Redirect
from django.core.cache import cache


class RedirectTests(TestCase):

    def setUp(self):
        self.redirect1 = Redirect.objects.create(key='Google', url='google.com.ar', active=True)
        self.redirect2 = Redirect.objects.create(key='Amazon', url='amazon.com', active=False)
        self.today = timezone.now().strftime("%Y-%m-%d %H:%M:%S")

    def test_create(self):
        goo = Redirect.objects.get(key="Google")
        self.assertEqual(goo.created_at.strftime("%Y-%m-%d %H:%M:%S"),self.today )
        self.assertEqual(goo.active,self.redirect1.active)
        self.assertEqual(goo.url,self.redirect1.url)
    
    def test_update(self):
        Redirect.objects.filter(key='Amazon').update(url='amazon.net')
        amaz=Redirect.objects.get(key="Amazon")
        self.assertEqual(amaz.updated_at.strftime("%Y-%m-%d %H:%M:%S"), self.today)
        self.assertNotEqual(amaz.url, self.redirect2.url)
        self.assertTrue(cache.has_key(self.redirect1.key))
        self.assertFalse(cache.has_key(self.redirect2.key))
