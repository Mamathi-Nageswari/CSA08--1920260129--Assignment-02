"""Q5 - Complete the Code: mutable default argument bug."""


def add_item_buggy(item, order=[]):
    order.append(item)
    return order


def add_item(item, order=None):
    # TODO 1
    if order is None:
        order = []
    order.append(item)
    return order


print(add_item_buggy("Tea"), add_item_buggy("Vada"))
print(add_item("Tea"), add_item("Vada"))
print("add_item_buggy.__defaults__ =", add_item_buggy.__defaults__)
print("add_item.__defaults__       =", add_item.__defaults__)
