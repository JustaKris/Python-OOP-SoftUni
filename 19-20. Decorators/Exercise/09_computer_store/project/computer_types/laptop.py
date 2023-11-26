from project.computer_types.computer import Computer


class Laptop(Computer):

    @property
    def processor_options(self):
        return {
            "AMD Ryzen 9 5950X": 900,
            "Intel Core i9-11900H": 1050,
            "Apple M1 Pro": 1200
        }

    @property
    def ram_options(self):
        return {
            2: 100,
            4: 200,
            8: 300,
            16: 400,
            32: 500,
            64: 600
        }

    @property
    def type_str(self):
        return 'laptop'
