from django.test import TestCase, Client
from django.urls import reverse_lazy
from core.models import Contact
from core.forms import ContactForm

# Create your tests here.


class TestContactView(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.client = Client()
        cls.url = reverse_lazy('core:contact')
        cls.response = cls.client.get(cls.url)
        cls.fake = {
            "name": "John",
            "email": "john@gmail.com",
            "subject": "Hello",
            "message": "Hello, how are you?"
        }

    def test_url(self):
        self.assertEqual(self.url, '/en/core/contact/')

    def test_template(self):
        self.assertTemplateUsed(self.response, 'contact.html')

    def test_form(self):
        self.assertIsInstance(self.response.context['form'], ContactForm)

    def test_form_valid(self):
        # response = self.client.post(self.url, data=self.fake)
        # print(response.context['form'])
        form = ContactForm(data=self.fake)
        self.assertTrue(form.is_valid())

    @classmethod
    def tearDownClass(cls) -> None:
        del cls.client
        

# class TestContactCase(TestCase):
#     @classmethod
#     def setUpClass(cls) -> None:
        
#         cls.data = {
#             "name": "John",
#             "email": "john@gmail.com",
#             "subject": "Hello",
#             "message": "Hello, how are you?"
#         }

#         Contact.objects.create(**cls.data)

#     def test_creation(self):
#         contact_obj = Contact.objects.first()

#         self.assertEqual(contact_obj.name, self.data["name"])
#         self.assertEqual(contact_obj.email, self.data["email"])
#         self.assertEqual(contact_obj.subject, self.data["subject"])
#         self.assertEqual(contact_obj.message, self.data["message"])

#     def test_str(self):
#         contact_obj = Contact.objects.first()
#         self.assertEqual(str(contact_obj), self.data["name"])

#     @classmethod
#     def tearDownClass(cls) -> None:
#         Contact.objects.all().delete()
#         del cls.data