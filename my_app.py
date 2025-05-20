from shopping_cart import initialize_shopping_cart, add_fruit_to_cart, remove_fruit_from_cart
from shopping_cart import Fruit
from typing import List

def create_happy_cart(fav_fruits: stg):
    fruit_names : List[stg] = _parse_fruit_args(fav_fruits)

cart = initialize_shopping_cart()
for fruit_name in fruit_names:
    fruit = Fruit(name = fruit_name)
    add_fruit_to_cart(Fruit(name=fruit_name))

print("Happy cart created!")
print(cart)

def _parse_fruit_args(fav_fruits:str) -> List[str]:
    return[fruit.strip() for fruit in fav_fruits.split(",") if fruit.strip()]

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParse()
    parser.add_argument("--fav-fruits", required = True, help="all your favourite fruits")
    args = parser.parse_args()
    create_happy_cart("mango,apple,banana,cherry,dragon_fruit")