from django.test import TestCase
from core.models import Contact

# Create your tests here.

class TestContactCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        
        cls.data = {
            "name": "John",
            "email": "john@gmail.com",
            "subject": "Hello",
            "message": "Hello, how are you?"
        }

        Contact.objects.create(**cls.data)

    def test_creation(self):
        contact_obj = Contact.objects.first()

        self.assertEqual(contact_obj.name, self.data["name"])
        self.assertEqual(contact_obj.email, self.data["email"])
        self.assertEqual(contact_obj.subject, self.data["subject"])
        self.assertEqual(contact_obj.message, self.data["message"])

    def test_str(self):
        contact_obj = Contact.objects.first()
        self.assertEqual(str(contact_obj), self.data["name"])

    @classmethod
    def tearDownClass(cls) -> None:
        Contact.objects.all().delete()
        del cls.data