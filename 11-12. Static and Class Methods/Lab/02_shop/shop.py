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
        if self.capacity <= sum(self.items.values()):
            return f"Not enough capacity in the shop"

        if item_name not in self.items:
            self.items[item_name] = 0
        self.items[item_name] += 1
        return f"{item_name} added to the shop"

    def remove_item(self, item_name: str, amount: int):
        if item_name not in self.items or self.items[item_name] < amount:
            return f"Cannot remove {amount} {item_name}"
        self.items[item_name] -= amount
        if self.items[item_name] == 0:
            del self.items[item_name]
        return f"{amount} {item_name} removed from the shop"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"
