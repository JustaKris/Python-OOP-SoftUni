from project.equipment.base_equipment import BaseEquipment


class ElbowPad(BaseEquipment):
    _protection = 90
    _price = 25.0

    def __init__(self):
        super().__init__(self._protection, self._price)

    def increase_price(self):
        self.price /= 1.1
