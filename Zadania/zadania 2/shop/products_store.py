
    products = {
        "chleb":{"quantity":100,
                 "price":3.5},

        "jabłka":{"quantity":50,
                  "price":3.2}
    }

def update_products_quantity(product_name, order_quantity):
    products[product_name]["quantity"] -= order_quantity