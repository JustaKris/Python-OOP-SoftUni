class Shop:
    def __init__(self, shop_name: str, shop_type: str, shop_capacity: int):
        self.name = shop_name
        self.type = shop_type
        self.capacity = shop_capacity
        self.items: dict[str, int] = {}  # {item_name: quantity}

    @classmethod
    def small_shop(cls, shop_name: str, shop_type: str):
        return cls(shop_name, shop_type, 10)

    def add_item(self, item_name: str):
        if item_name not in self.items:
            self.items[item_name] = 0
        self.items[item_name] += 1

