from django import forms
from .models import Post, Category


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

    def clean_content(self):
        content = self.cleaned_data["content"]

        if len(content) < 50:
            raise forms.ValidationError(
                "Минимум 50 символов"
            )

        return content


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"