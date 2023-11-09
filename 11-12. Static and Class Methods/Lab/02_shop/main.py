from shop import Shop


def main():
    fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)
    small_shop = Shop.small_shop("Fashion Boutique", "Clothes")
    print(fresh_shop)
    print(small_shop)
    print(fresh_shop.add_item("Bananas"))
    print(fresh_shop.remove_item("Tomatoes", 2))
    print(small_shop.add_item("Jeans"))
    print(small_shop.add_item("Jeans"))
    print(small_shop.remove_item("Jeans", 2))
    print(small_shop.items)


if __name__ == '__main__':
    main()
