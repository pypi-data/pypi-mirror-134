## Webhooks events

#### Stripe listen example: 

stripe listen --forward-to localhost:8000/webhooks/events/

#### Events that can be triggered
    customer.created
    issuing_card.created
    invoice.payment_failed
    customer.source.created
    payment_intent.succeeded
    payment_method.attached


#### Statuses for listing subs
```
    active
    past_due
    unpaid
    canceled
    xc
    incomplete_expired
    trialing
    all
    ended
```
# rent-insider-payments
