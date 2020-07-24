from django import forms
from wtpixel.models import Image
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, HTML


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'image')
        def save(self):
            image = super(ImageForm, self).save()
            return image
