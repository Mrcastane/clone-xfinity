from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home_view, name ="home"),
    path("billing/", views.billing_view, name ="billing"),
    path("info/", views.info_view, name ="info"),
    path("thankyou/", views.thank_you_view, name ="thank-you"),
]
