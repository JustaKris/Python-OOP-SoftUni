class Shop:
    def __init__(self, shop_name: str, shop_type: str, shop_capacity: int):
        self.name = shop_name
        self.type = shop_type
        self.capacity = shop_capacity
        self.items: dict[str, int] = {}  # {item_name: quantity}

    def 
