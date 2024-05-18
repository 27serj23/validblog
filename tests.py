from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from .models import Post, Comment
from .forms import PostForm, CommentForm


# Create your tests here.
class PostModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        Post.objects.create(title="Test Title", content="Test Content")

    def test_post_str_representation(self):
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field('title').max_length
        self.assertEqual(max_length, 200)

    def test_content_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('content').verbose_name
        self.assertEqual(field_label, 'content')

    def test_title_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

class PostViewsTests(TestCase):
    def test_post_list_view(self):
        response = self.client.get(reverse('list'))
        self.assertEqual(response.status_code, 200)

    def test_post_create_view(self):
        response = self.client.get(reverse('create'))
        self.assertEqual(response.status_code, 200)


class PostFormTests(TestCase):
    def test_post_form_validation(self):
        form_data = {'title': '', 'content': 'Some content'}
        form = PostForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_comment_form_validation(self):
        form_data = {'author': 'Test Author', 'content': ''}
        form = CommentForm(data=form_data)
        self.assertFalse(form.is_valid())

