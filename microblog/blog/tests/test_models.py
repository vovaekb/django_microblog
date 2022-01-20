from django.test import TestCase
from blog.models import Post

class ModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Post.objects.create(text="Some simple text")

    def test_string_method(self):
        post = Post.objects.get(id=1)
        self.assertEqual(str(post), "Text: Some simple text")