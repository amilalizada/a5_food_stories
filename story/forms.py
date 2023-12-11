from django import forms
from story.models import Recipe



class CreateRecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = [
            'title',
            'content',
            'description',
            'image',
            'category',
            'tags',
        ]
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Title"
            }),
            "content": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Content"
            }),
            "description": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Description",
                "rows": 10,
                "cols": 30
            }),
        }
        # labels = [
        #     "Name",
        #     "Surname",
        #     "Email",
        #     "Subject",
        #     "Message",
        # ]

    