from project.equipment.base_equipment import BaseEquipment


class KneePad(BaseEquipment):
    _protection = 120
    _price = 15.0

    def __init__(self):
        super().__init__(self._protection, self._price)

    def increase_price(self):
        self.price /= 1.2
