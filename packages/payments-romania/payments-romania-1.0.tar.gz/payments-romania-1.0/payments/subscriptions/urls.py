from django.urls import path

from payments.subscriptions import views

urlpatterns = [
    path('create-sub/', views.create_sub),
    path('cancel-subscription/', views.cancel_subscription),
    path('subscription-list/', views.subscription_list),
    path('subscription-alteration/', views.subscription_alteration),
]
