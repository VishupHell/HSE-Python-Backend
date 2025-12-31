from hw1.models.product import Product


def select_products_by_category(products: list[Product], category: str) -> list[Product]:
    return list(filter(lambda p: p.category == category, products))
