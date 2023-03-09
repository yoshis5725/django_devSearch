from django.forms import ModelForm
from django import forms
from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'featured_image', 'demo_link', 'source_link', 'tags']

        # customizing/overwriting the classes
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input'}),
            'description': forms.Textarea(attrs={'class': 'input'}),
            'featured_image': forms.FileInput(attrs={'class': 'input'}),
            'demo_link': forms.TextInput(attrs={'class': 'input'}),
            'source_link': forms.TextInput(attrs={'class': 'input'}),
            'tags': forms.CheckboxSelectMultiple(attrs={'class': 'input'}),
        }


