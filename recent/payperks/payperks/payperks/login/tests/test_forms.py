from django.test import TestCase, Client
from login.forms import RegistrationForm


class TestRegister(TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_valid_data(self):
        form_data = {
            'username': 'test user',
            'email': 'test@te.st',
            'password1': 'test',
            'password2': 'test',
            'city': 'test',
            'state': 'test',
            'zip_code': 'test'
        }
        form = RegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())

    # def test_blank_data(self):
    #     form = CommentForm({}, entry=self.entry)
    #     self.assertFalse(form.is_valid())
    #     self.assertEqual(form.errors, {
    #         'name': ['required'],
    #         'email': ['required'],
    #         'body': ['required'],
    #     })

    # def test_register_form(self):
    #     form_data = {
    #         'username': 'test user',
    #         'email': 'test@te.st',
    #         'password1': 'test',
    #         'password2': 'test',
    #         'city': 'test',
    #         'state': 'test',
    #         'zip_code': 'test'
    #     }
    #     form = RegistrationForm(data=form_data)
    #     self.assertTrue(form.is_valid())

    #     response = self.client.post("/register/", form_data)
    #     self.assertEqual(response.status_code, 200)

    #     self.assertFormError(response,
    #                          'form', 'something', 'This field is required.')
    #     # Check that the response is 200 OK.
    #     self.assertEqual(response.status_code, 200)

    #     # Check that the rendered context contains 5 customers.
    #     self.assertEqual(len(response.context['customers']), 5)


# class MyTests(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         # Set up data for the whole TestCase
#         cls.user = Foo.objects.create(bar="Test")
#         ...
#
#     def test1(self):
#         # Some test using self.foo
#         ...
#
#     def test2(self):
#         # Some other test using self.foo
