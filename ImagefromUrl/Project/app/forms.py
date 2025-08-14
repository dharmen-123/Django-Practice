from django.forms import ModelForm
from .models import URLImage

class Imgform(ModelForm):
    class Meta:
        model=URLImage
        fields='__all__'