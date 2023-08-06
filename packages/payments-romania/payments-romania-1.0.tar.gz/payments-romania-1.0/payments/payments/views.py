import datetime
import stripe

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

KEY = stripe.api_key = 'sk_test_51K70bDJrktwvdD84D4Y45kSYHKA0dHvfb' \
                       'on0Xnog4Ib54emyy44jbgEJlNqv6f7KV99UkSc7ss7RYid' \
                       'EBdXgMwef00oT3RSCrU'


@api_view(['POST'])
def create_customer_payment_method(request):
    # here we create a new customer
    test_customer = stripe.Customer.create(
        description="Test Customer",
        email="test@test.ro",
    )
    # here we create a new payment method
    payment_method_create_card = stripe.PaymentMethod.create(
        type="card",
        card={
            "number": "4242424242424242",
            "exp_month": 12,
            "exp_year": 2022,
            "cvc": "314",
        },
    )

    # here we attach the payment method for the customer
    stripe.PaymentMethod.attach(
        payment_method_create_card.stripe_id,
        customer=test_customer.stripe_id,
    )

    # here we modify the default payment method for test_customer
    stripe.Customer.modify(
        test_customer.stripe_id,
        invoice_settings={"default_payment_method":
                          payment_method_create_card.stripe_id},
    )

    return Response(status=status.HTTP_200_OK, data=test_customer)


@api_view(['POST'])
def create_products(request):
    """
        Here we create two products for subscription usage
    """
    # here we create the first product for future subscriptions
    product_gold = stripe.Product.create(
        name="Gold Special",
    )
    # here we create a price and other data for the first product
    stripe.Price.create(
        unit_amount=2000,
        currency="ron",
        recurring={"interval": "month"},
        product=product_gold.stripe_id,
    )

    # here we create the second product for future subscriptions
    product_silver = stripe.Product.create(
        name="Silver Advance",
    )
    # here we create a price and other data for the second product
    stripe.Price.create(
        unit_amount=1000,
        currency="ron",
        recurring={"interval": "month"},
        product=product_silver.stripe_id,
    )
    return Response(status=status.HTTP_200_OK,
                    data=product_gold | product_silver)


def refund_helper(charge, percent):
    """
        This function is a helper for refund_customer.
        We create a Refund object based on charge object and percent.
    """
    refund = stripe.Refund.create(
        charge=charge["id"],
        amount=int(charge["amount"] * percent),
        reason="requested_by_customer"
    )
    return Response(status=status.HTTP_204_NO_CONTENT, data=refund)


@api_view(['POST'])
def refund_customer(request):
    """
        This function refunds the customer based on how many days
         have passed since the begging on the month.
         We refund the customer as it follows:
         1-5 100% $
         6-10 75% $
         15-17 50% $
         17-end 0% $
    """

    customer_id = [x for x in stripe.Customer.list(limit=3)["data"]
                   if x["description"] == "Test Customer"][0]["id"]

    charge = stripe.Charge.list(limit=3)["data"][2] if\
        stripe.Charge.list(limit=3)["data"][0]["customer"]\
        == customer_id else None

    if datetime.datetime.now().day in [x for x in range(1, 6)]:
        return refund_helper(charge, 1)
    elif datetime.datetime.now().day in [x for x in range(6, 11)]:
        return refund_helper(charge, 0.75)
    elif datetime.datetime.now().day in [x for x in range(15, 18)]:
        return refund_helper(charge, 0.5)
    else:
        return Response(
            status=status.HTTP_403_FORBIDDEN, data={
                "refund": "we can only refund a customer if"
                          " sum is greater then 1"})


@api_view(['POST'])
def change_card_details(request):
    customer_id = "cus_KnH5alP1AzYqDL"
    customer_object = stripe.Customer.retrieve(customer_id)
    if not stripe.Subscription.list(limit=300, status="unpaid",
                                    customer=customer_id):
        card = stripe.Customer.retrieve_source(
            customer_id,
            "card_1K7gukJrktwvdD84JBn6UFWw",
        )


@api_view(['GET'])
def check_unpaid_invoices_customer(request):
    customer_id = [x for x in stripe.Customer.list(limit=3)["data"]
                   if x["description"] == "Test Customer"][0]["id"]
    customer_invoices = stripe.Invoice.list(limit=200, customer=customer_id,
                                            status='uncollectible')
    return Response(status=200, data=customer_invoices)
