# 💳 DynamiCore Billing Layer (Stripe-ready)

PLANS = {
    "free": {
        "limit": 1000
    },
    "pro": {
        "limit": 10000
    },
    "enterprise": {
        "limit": 100000
    }
}

def get_plan_limit(plan: str):
    return PLANS.get(plan, PLANS["free"])["limit"]


def create_checkout_mock(user_id: str, plan: str):
    """
    Placeholder de Stripe Checkout.
    Luego lo conectamos a Stripe real.
    """
    return {
        "checkout_url": f"https://checkout.stripe.com/mock/{user_id}/{plan}",
        "plan": plan
                         }
