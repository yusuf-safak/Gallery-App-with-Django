from django.urls import path
from .views import *
urlpatterns = [
    path('',images_view),
    path('detail/<int:id>', detail_view),
    path('create/', create_view),
    path('submitForm/', submitForm_views),
    path('delete/<int:id>',delete_view),
]
