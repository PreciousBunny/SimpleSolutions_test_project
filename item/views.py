import stripe
from django.views.generic import ListView
from django.conf import settings
from django.shortcuts import redirect, render
from django.views import View

from item.models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY
REDIRECT_DOMAIN = 'http://127.0.0.1:8000'


# Create your views here.
class ItemListView(ListView):
    model = Item
    extra_context = {
        'title': 'Все категории',
        'object_list': Item.objects.all()
    }
    context_object_name = "items"
    template_name = "item/item_list.html"


class CreateStripeCheckoutSessionView(View):
    """
    Create a checkout session and redirect the user to Stripe's checkout page
    """

    def post(self, request, *args, **kwargs):
        price = Item.objects.get(id=self.kwargs["pk"])

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "currency": "usd",
                        "unit_amount": int(price.price) * 100,
                        "product_data": {
                            "name": price.name,
                            "description": price.description,

                        },
                    },
                    "quantity": 1,
                }
            ],
            mode='payment',
            customer_creation='always',
            success_url=REDIRECT_DOMAIN + '/payment_successful?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=REDIRECT_DOMAIN + '/payment_cancelled',
        )
        return redirect(checkout_session.url, code=303)

# use Stripe dummy card: 4242 4242 4242 4242


def payment_successful(request):
    checkout_session_id = request.GET.get('session_id', None)
    session = stripe.checkout.Session.retrieve(checkout_session_id)
    customer = stripe.Customer.retrieve(session.customer)

    return render(request, 'item/payment_successful.html', {'customer': customer})


def payment_cancelled(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY_TEST
    return render(request, 'item/payment_cancelled.html')
