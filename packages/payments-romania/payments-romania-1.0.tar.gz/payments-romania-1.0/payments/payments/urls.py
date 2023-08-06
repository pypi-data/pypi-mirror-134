from django.urls import path

from payments.payments import views

urlpatterns = [
    path('create-products/', views.create_products),
    path('create-customer/', views.create_customer_payment_method),
    path('change-card-details/', views.change_card_details),
    path('refund/', views.refund_customer),
    path('check-unpaid-invoices/', views.check_unpaid_invoices_customer),
]
