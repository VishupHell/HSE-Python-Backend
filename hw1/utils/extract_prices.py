from hw1.models.product import Product


def extract_prices(products: list[Product])-> list[float]:
    return [i.get_price() for i in products]
