import stripe
import logging

from rest_framework.response import Response
from rest_framework.decorators import api_view


ENDPOINT_SECRET = 'whsec_BoDAsE6ruehGJAN78uSktD7pGJMMkBOJ'

logger = logging.getLogger(__name__)


@api_view(['POST'])
def events(request):
    """
        stripe listen --forward-to http://127.0.0.1:8000/
            webhooks/events/
        stripe trigger customer.created(to mock this action)
        SEE:
        https://stripe.com/docs/api/events/types
    """
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, ENDPOINT_SECRET
        )
        events = stripe.Event.list()
        # print(events)
    except ValueError as e:
        logger.info(e)
        # Invalid payload
        return Response(status=400)
    except stripe.error.SignatureVerificationError as e:
        logger.info(e)
        # Invalid signature
        return Response(status=400)

    # Handle the event, from here we can send an email, store in the db
    # some information
    if event.type == 'customer.created':
        # Occurs whenever a new customer is created.
        customer = event.data.object
        logger.info(customer)
    if event.type == 'issuing_card.created':
        # Occurs whenever a card is created.
        card = event.data.object
        logger.info(card)
    if event.type == 'invoice.payment_failed':
        # Occurs whenever an invoice payment attempt fails,
        # due either to a declined payment or to the lack of a
        # stored payment method
        unpaid_sub = event.data.object
        logger.info(unpaid_sub)
    if event.type == 'customer.source.created':
        # Occurs whenever a new source(a customer's payment instrument)
        # is created for a customer.
        money_source = event.data.object
        logger.info(money_source)
    if event.type == 'payment_intent.succeeded':
        payment_intent = event.data.object  # contains a stripe.PaymentIntent
        logger.info(payment_intent)
    if event.type == 'payment_method.attached':
        payment_method = event.data.object  # contains a stripe.PaymentMethod
        logger.info(payment_method)
    # ... handle other event types
    else:
        logger.info('Unhandled event type {}'.format(event.type))

    return Response(status=200, data=events)
