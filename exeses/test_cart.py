import pytest
from cart import Cart
def test_cart():
    cart = Cart()
    cart.add({"product": "Mere", "quantity": 2 , "price" : 3})
    total = cart.calculate_total()
    assert total == 6
def test_empty_cart():
    cart = Cart()
    total = cart.calculate_total()
    assert total == 0

