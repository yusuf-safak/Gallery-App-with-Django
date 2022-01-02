from django.contrib import admin
from .models import image

class adminImage(admin.ModelAdmin):
    list_display = ["imageTitle","imageDateTime"]
    class Meta:
        model = image
# Register your models here.
admin.site.register(image)
