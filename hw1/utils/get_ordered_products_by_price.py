from hw1.models.product import Product


def get_ordered_products_by_price(products: list[Product]) -> list[Product]:
    return sorted(products, key=lambda c: c.get_price(), reverse=True)
