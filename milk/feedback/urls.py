from django.urls import path, include

from .views import ContactFormsView, thanks

urlpatterns = [
    path('', ContactFormsView.as_view(), name='contact'),
    path('thanks/', thanks, name='thanks'),
]
