from django import forms

from .models import Blog


class SearchForm(forms.Form):
    search = forms.CharField(
        label="",
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-control me-2", "placeholder": "Search"}
        ),
    )


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["title", "content", "category"]
