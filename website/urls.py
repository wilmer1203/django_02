# Todas las urls de la aplicación website

from django.urls import path
from website.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]
