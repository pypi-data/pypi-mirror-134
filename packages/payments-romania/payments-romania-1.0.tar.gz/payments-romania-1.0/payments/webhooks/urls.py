from django.urls import path

from payments.webhooks import views

urlpatterns = [
    path('events/', views.events),
]
