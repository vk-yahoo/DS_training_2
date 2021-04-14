import time
import random
from model.customer import Customer
from model.product import Product
from model.user import User


def current_time_millis():
    return int(round(time.time() * 1000))


valid_customers = [Customer(
    firstname="Adam",
    lastname="Smith",
    phone="+0123456789",
    address="Hidden Place",
    postcode="12345",
    city="New City",
    country="US",
    zone="KS",
    email="adam%s@smith.me" % current_time_millis(),
    password="qwerty"),
                   # ...
    ]

valid_users = [User(
    firstname="Adam",
    lastname="Smith",
    phone="+0123456789",
    address="Hidden Place",
    postcode="12345",
    city="New City",
    country="US",
    email="adam%s@smith.me" % current_time_millis(),
    password="qwerty"
)]

valid_products = [Product(
    title="product_" + str(current_time_millis()),
    code=str(current_time_millis()),
    quantity=random.randint(1, 100),
    keywords="Keywords list",
    short_description="Short description",
    long_description="Long description",
    head_title="Head title",
    meta_description="Meta description",
    purchase_price=random.randint(10, 60)
)]
