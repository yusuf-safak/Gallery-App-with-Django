from django.forms import ModelForm, fields
from .models import image
class createForm(ModelForm):
    class Meta:
        model = image
        fields = '__all__'
