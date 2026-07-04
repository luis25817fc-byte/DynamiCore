import stripe
import os

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")


def create_checkout(api_key: str):
    session = stripe.checkout.Session.create(
        mode="subscription",
        line_items=[{
            "price_data": {
                "currency": "usd",
                "product_data": {
                    "name": "DynamiCore Pro"
                },
                "unit_amount": 1999,
                "recurring": {
                    "interval": "month"
                }
            },
            "quantity": 1
        }],
        success_url="https://dynamicore.onrender.com/success",
        cancel_url="https://dynamicore.onrender.com/cancel",
        metadata={"api_key": api_key}
    )

    return session.url
