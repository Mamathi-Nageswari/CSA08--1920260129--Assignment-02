"""Q5 - Order functions: positional/keyword/default params, returning two values, scope."""
GST_RATE = 0.05
PRICES = {"Tea": 12, "Vada": 15, "Dosa": 40, "Coffee": 15}
orders_served = 0


def add_item(item, qty=1, order=None):
    """item positional (always needed), qty default 1, order keyword (optional)."""
    if order is None:
        order = []
    order.append((item, qty))
    return order


def bill(order, gst_rate=GST_RATE):
    """Returns two values as a tuple: (subtotal, gst)."""
    subtotal = sum(PRICES[item] * qty for item, qty in order)
    return subtotal, round(subtotal * gst_rate, 2)


def serve(order):
    global orders_served            # needed to rebind a module-level name
    orders_served += 1


def make_counter():
    count = 0                       # enclosing (nonlocal) name

    def next_token():
        nonlocal count
        count += 1
        return count
    return next_token


token = make_counter()
for customer, wanted in [("A", [("Tea", 2)]), ("B", [("Dosa", 1), ("Coffee", 1)]), ("C", [("Vada", 3)])]:
    order = None
    for item, qty in wanted:
        order = add_item(item, qty=qty, order=order)
    subtotal, gst = bill(order)
    serve(order)
    print(f"customer {customer} token {token()}: {order} subtotal Rs{subtotal} gst Rs{gst}")
print("orders_served (global) =", orders_served)


def shadow():
    GST_RATE = 0.18                 # local: does not change the global
    return GST_RATE


print("local GST_RATE", shadow(), "| global GST_RATE", GST_RATE)
