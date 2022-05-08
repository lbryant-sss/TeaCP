from django.forms import ModelForm

from blogapp.models import ArticlePost

class CreatorForm:
    class Meta:
        fields = [
            'title',
            'slug',
            'body',
            'image',
        ]