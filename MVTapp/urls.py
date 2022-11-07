from django.urls import path
from MVTapp.views import *

urlpatterns = [
    
    path('padre/', Padre),
    path('madre/', Madre),
    path('hermano/', Hermano)
]