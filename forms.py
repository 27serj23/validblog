from django import forms
from .models import Comment, Post
from django.core.exceptions import ValidationError
from datetime import date


class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=200, required=True)
    content = forms.CharField(max_length=5000, required=True)

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title:
            raise ValidationError("Title can't be empty")
        # Additional validation for special characters and HTML tags can be added here
        return title

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if not content:
            raise ValidationError("Content can't be empty")
        # Additional validation for special characters and HTML tags can be added here
        return content

    class PostForm(forms.Form):
        publish_date = forms.DateField()

        def clean_publish_date(self):
            publish_date = self.cleaned_data.get('publish_date')
            if publish_date < date.today():
                raise ValidationError("Publish date can't be in the past")
            # Additional validation for date format can be added here
            return publish_date

    class Meta:
        model = Post
        fields = ['title', 'content']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['post', 'author', 'content', 'date_created']


