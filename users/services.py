import stripe

import config.settings

stripe.api_key = config.settings.STRIPE_API_KEY


def create_stripe_product(product_name):
    """ Создание продукта в stripe. Принимает имя продукта из модели урока или курса, возвращает id продукта """
    stripe_product = stripe.Product.create(name=product_name)
    return stripe_product.id


def create_stripe_price(payment_amount, stripe_product_id):
    """ Создание цены в stripe. Принимает стоимость продукта из модели уроков или курса и id продукта stripe, возвращает id цены stripe """
    stripe_price = stripe.Price.create(
        currency='rub',
        unit_amount=payment_amount * 100,
        product_data={'name': stripe_product_id},
    )
    return stripe_price.id


def create_stripe_session(stripe_price_id):
    """ Создание сессии для оплаты в stripe. Принимает id цены stripe, возвращает id сессии stripe и url сессии stripe """
    stripe_session = stripe.checkout.Session.create(
        success_url='http://127.0.0.1:8000/',  # можно без него посмотреть при отработке
        line_items=[{'price': stripe_price_id, 'quantity': 1}],
        mode="payment",
    )
    return stripe_session['url'], stripe_session['id']


def checkout_stripe_session(stripe_session_id):
    """ Получение статуса сессии stripe. Принимает id сессии stripe возвращает status сессии stripe """
    checkout_session = stripe.checkout.Session.retrieve(
        stripe_session_id,
    )
    print(checkout_session)
    return checkout_session['status']
