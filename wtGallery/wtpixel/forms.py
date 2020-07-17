from django import forms
from wtpixel.models import Image


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('description', 'image')