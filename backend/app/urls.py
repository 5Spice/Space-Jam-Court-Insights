"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# urls.py

from django.urls import path, re_path
from django.http import HttpResponse  # Import HttpResponse
from app.views import players

# Define a simple view function
def home_view(request):
    return HttpResponse("This is the homepage.")

urlpatterns = [
    path('', home_view, name='home'),  # Add this root URL pattern
    re_path(r'^api/v1/playerSummary/(?P<playerID>[0-9]+)$', players.PlayerSummary.as_view(), name='player_summary'),
]

