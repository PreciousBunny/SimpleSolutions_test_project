from django.urls import path


from item.apps import ItemConfig
from item.views import ItemListView, CreateStripeCheckoutSessionView, payment_successful, payment_cancelled

app_name = ItemConfig.name


urlpatterns = [
    path('item/', ItemListView.as_view(), name='item_list'),
    path('buy/<int:pk>/', CreateStripeCheckoutSessionView.as_view(), name="create-checkout-session"),
    path('payment_successful/', payment_successful, name='payment_successful'),
    path('payment_cancelled/', payment_cancelled, name='payment_cancelled'),
]
