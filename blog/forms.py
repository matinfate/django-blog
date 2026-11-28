from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "body"]
        labels = {
            "title": "عنوان",
            "body": "متن",
        }
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "عنوان پست…"}),
            "body": forms.Textarea(attrs={"placeholder": "متن پست…", "rows": 8}),
        }
