from django import forms
from .models import *

class AnimeForms(forms.ModelForm):
    class Meta:
            localized_fields = '__all__'
            model = Anime
            fields = ['image_url']
            widgets = {
            'image_url': forms.TextInput(
                attrs={
                    'id': 'liveimg',
                    'onkeyup': 'changeValue()',
                    'style': 'width:274px'
                    }
                ),
        }
            
class EpisodeForms(forms.ModelForm):
    class Meta:
            localized_fields = '__all__'
            model = Episode
            fields = ['image_url']
            widgets = {
            'image_url': forms.TextInput(
                attrs={
                    'id': 'liveimg',
                    'onkeyup': 'changeValue()',
                    'style': 'width:274px'
                    }
                ),
        }
