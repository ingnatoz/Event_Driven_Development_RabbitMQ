from .meli import Meli
from apps.products.api.producer import publish


def get_meli_obj():
    CLIENT_ID = "123"
    CLIENT_SECRET = "a secret"
    ACCESS_TOKEN = "a access_token"
    REFRESH_TOKEN = "a refresh_token"
    meli_obj = Meli(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, access_token=ACCESS_TOKEN,
                         refresh_token=REFRESH_TOKEN, site_id='MLM')
    return meli_obj


def get_product_list():
    meli_obj = get_meli_obj()
    response = meli_obj.get(
        '/users/1234/items/search',
        {'search_type': 'scan', 'access_token': meli_obj.access_token, 'logistic_type': 'fulfillment'}
    )
    content = response.json()
    # RabbitMQ cloudamqp
    publish('access_token', content)
    return content


def get_product_by_id(ml_product_id):
    # https://api.mercadolibre.com/items?ids=MLA599260060,MLA594239600
    meli_obj = get_meli_obj()
    response = meli_obj.get(
        "/items/" + ml_product_id,
        {'include_attributes': 'all', 'access_token': meli_obj.access_token}
    )
    content = response.json()
    # RabbitMQ cloudamqp
    publish('get_product_by_id', content)
    return content
