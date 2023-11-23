from django import forms
from core.models import Contact



class ContactForm(forms.ModelForm):

    surname = forms.CharField(required=False, widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Your Surname"
    }))

    class Meta:
        model = Contact
        fields = [
            'name',
            'surname',
            'email',
            'subject',
            'message',
        ]
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Your Name"
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Your Email"
            }),
            "subject": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Subject"
            }),
            "message": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Message",
                "cols": 30,
                "rows": 7
            })  
        }
        labels = [
            "Name",
            "Surname",
            "Email",
            "Subject",
            "Message",
        ]

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        if name == "abc":
            self.add_error("name", "Name cannot be abc")

        return super().clean()

    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not email.endswith(".com"):
            raise forms.ValidationError("Enter a valid email address")
        return email
    
    def clean_message(self):
        message = self.cleaned_data.get("message")
        if not " " in message:
            raise forms.ValidationError("Enter a valid message")
        return message


    