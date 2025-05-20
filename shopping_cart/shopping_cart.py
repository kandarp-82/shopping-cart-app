from dataclasses import dataclass
from typing import List
from .fruit import Fruit


@dataclass
class ShoppingCart:
    items: List[Fruit]
    price: float = None

def initialize_shopping_cart() -> ShoppingCart:
    """
    Initialize a new ShoppingCart object
    """
    return ShoppingCart(items=[])

def add_fruit_to_cart(cart:ShoppingCart, fruit:Fruit) -> None:
    """
    Add fruit to Cart
    """
    cart.items.append(fruit)
def remove_fruit_from_cart(cart:ShoppingCart,fruit_name:str) -> None:
    """
    Remove fruit from the cart
    """
    for idx, items in enumerates(cart.items):
        if items.names == fruit_name:
            return cart.items.pop(idx)
    return None
