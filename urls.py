from django.urls import path
from . import views

urlpatterns = [
   path("christmas", views.christmas)

]