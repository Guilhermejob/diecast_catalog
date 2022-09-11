from django.urls import path
from .views import UsersView


urlpatterns = [
    path('registration/', UsersView.as_view())
]
