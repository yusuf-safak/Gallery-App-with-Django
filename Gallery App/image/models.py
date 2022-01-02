from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class image(models.Model):
    imageTitle = models.CharField(max_length=120)
    imageText = RichTextField()
    image = models.ImageField(null=True,blank=True)
    imageDateTime = models.DateTimeField(auto_now_add=True)