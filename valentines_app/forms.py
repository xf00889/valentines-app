from django import forms
from .models import LoveLetter, GalleryImage
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field

class LoveLetterForm(forms.ModelForm):
    class Meta:
        model = LoveLetter
        fields = ['title', 'content', 'background_music']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'handwritten-font'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'love-letter-form'
        self.helper.add_input(Submit('submit', 'Save Love Letter', css_class='btn-love'))
        self.helper.layout = Layout(
            Field('title', css_class='form-control-love'),
            Field('content', css_class='form-control-love handwritten-font'),
            Field('background_music', css_class='form-control-love'),
        )

class GalleryImageForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = ['title', 'image', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'gallery-form'
        self.helper.add_input(Submit('submit', 'Upload Image', css_class='btn-love'))
        self.helper.layout = Layout(
            Field('title', css_class='form-control-love'),
            Field('image', css_class='form-control-love'),
            Field('description', css_class='form-control-love'),
        ) 