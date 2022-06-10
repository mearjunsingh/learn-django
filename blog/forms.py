from django import forms

from ckeditor.widgets import CKEditorWidget

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
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": CKEditorWidget(),
            "category": forms.Select(attrs={"class": "form-control"}),
        }
