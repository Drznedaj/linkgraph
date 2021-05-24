from django.test import TestCase, Client
from django.contrib.auth import get_user_model, authenticate
from .models import Writer, Article


class WriterTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test', password='12test12', email='test@example.com')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_correct_login(self):
        user = authenticate(username='test', password='12test12')
        self.assertTrue((user is not None) and user.is_authenticated, "User with correct credentials not authenticated!")

    def test_wrong_username(self):
        user = authenticate(username='wrong', password='12test12')
        self.assertFalse(user is not None and user.is_authenticated, "User with incorrect username authenticated!")

    def test_wrong_pssword(self):
        user = authenticate(username='test', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated, "User with incorrect password authenticated!")

    def test_is_editor_set(self):
        self.user.is_editor = True
        self.assertIsInstance(self.user, Writer, "User is not Writer class!")
        self.assertEqual(self.user.is_editor, True, "User is_editor not set properly!")


class ArticleTest(TestCase):

    def setUp(self):
        self.writer = get_user_model().objects.create_user(username='writer', password='12test12', email='test@example.com')
        self.editor = get_user_model().objects.create_user(username='editor', password='12test12', email='test@example.com')
        self.writer.save()
        self.editor.save()
        self.article = Article(title='Test', content='testtesttesttest', written_by=self.writer)
        self.article.save()

    def tearDown(self):
        self.writer.delete()
        self.editor.delete()
        self.article.delete()

    def test_editor_is_none(self):
        self.assertIsNone(self.article.edited_by, 'Edited by field is not none before setting!')

    def test_article_writer(self):
        self.assertEqual(self.article.written_by, self.writer)


class ViewsTest(TestCase):

    def setUp(self):
        self.writer = get_user_model().objects.create_user(username='writer', password='12test12', email='test@example.com')
        self.editor = get_user_model().objects.create_user(username='editor', password='12test12', email='test@example.com', is_editor=True)
        self.writer.save()
        self.editor.save()
        self.editor_client = Client()
        self.client.login(username='writer', password='12test12')
        self.editor_client.login(username='editor', password='12test12')
        self.dashboard_url = "/"
        self.edit_url = "/article-approval/"
        self.edited_url = "/articles-edited/"

    def tearDown(self):
        self.writer.delete()
        self.editor.delete()

    def test_dashboard_get(self):
        response = self.client.get(self.dashboard_url)
        eresponse = self.editor_client.get(self.dashboard_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(eresponse.status_code, 200)

    def test_approval_get(self):
        response = self.client.get(self.edit_url)
        eresponse = self.editor_client.get(self.edit_url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(eresponse.status_code, 200)

    def test_edited_get(self):
        response = self.client.get(self.edit_url)
        eresponse = self.editor_client.get(self.edit_url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(eresponse.status_code, 200)
