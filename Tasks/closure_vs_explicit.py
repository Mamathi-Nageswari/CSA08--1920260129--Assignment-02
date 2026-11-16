"""Q5 - Alternative concept: always pass the list explicitly, or keep it in a closure."""
import sys


def add_item_explicit(item, order):
    order.append(item)
    return order


def new_order():
    items = []

    def add(item):
        items.append(item)
        return items
    return add


a, b = [], []
add_item_explicit("Tea", a); add_item_explicit("Vada", b)
print("explicit:", a, b)
c1, c2 = new_order(), new_order()
c1("Tea"); print("closure :", c1("Coffee"), c2("Vada"))
print("space per customer: list", sys.getsizeof([]), "B | closure function",
      sys.getsizeof(c1) + sys.getsizeof(c1.__closure__[0]), "B + list", sys.getsizeof([]), "B")
