from project.computer_types.computer import Computer


class DesktopComputer(Computer):

    @property
    def processor_options(self):
        return {
            "AMD Ryzen 7 5700G": 500,
            "Intel Core i5-12600K": 600,
            "Apple M1 Max": 1800
        }

    @property
    def ram_options(self):
        return {
            2: 100,
            4: 200,
            8: 300,
            16: 400,
            32: 500,
            64: 600,
            128: 700
        }

    @property
    def type_str(self):
        return 'desktop computer'
