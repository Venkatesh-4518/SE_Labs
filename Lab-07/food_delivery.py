
import math


def parse_order(items_csv):
    order = {}

    if not isinstance(items_csv, str):
        return order

    for item in items_csv.split(','):
        if ':' not in item:
            continue

        name, qty = item.split(':', 1)
        name = name.strip()
        qty = qty.strip()

        try:
            quantity = int(qty)

            if name and quantity > 0:
                order[name] = quantity

        except ValueError:
            continue

    return order


def delivery_eta(distance_km):
    try:
        distance = float(distance_km)

        if not math.isfinite(distance) or distance < 0:
            return 15

        return int(15 + distance * 4)

    except (ValueError, TypeError):
        return 15


def coupon_discount(code):
    if not isinstance(code, str):
        return 0

    code = code.strip().upper()

    if not code.startswith('SAVE'):
        return 0

    discount = code[4:]

    if not discount.isdigit():
        return 0

    discount = int(discount)

    if 0 <= discount <= 100:
        return discount

    return 0


def main():
    print("==== Running parse_order ====")
    user_input = input(
        "Enter items as name:qty CSV (e.g. pizza:2,burger:1): "
    )
    result = parse_order(user_input)
    print("Order:", result)

    print("\n==== Running delivery_eta ====")
    user_input = input("Enter distance in km (e.g. 4.5): ")
    result = delivery_eta(user_input)
    print("ETA in Minutes:", result)

    print("\n==== Running coupon_discount ====")
    user_input = input("Enter a coupon code (e.g. SAVE50): ")
    result = coupon_discount(user_input)
    print("Discount:", result)


if __name__ == "__main__":
    main()
