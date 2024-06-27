class Car:
    def __init__(self, model, year, manufacturer, engine_capacity, color, price):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine_capacity = engine_capacity
        self.color = color
        self.price = price

    def set_data(self, model, year, manufacturer, engine_capacity, color, price):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine_capacity = engine_capacity
        self.color = color
        self.price = price

    def get_data(self):
        return {
            'model': self.model,
            'year': self.year,
            'manufacturer': self.manufacturer,
            'engine_capacity': self.engine_capacity,
            'color': self.color,
            'price': self.price
        }

    def get_model(self):
        return self.model

    def set_model(self, model):
        self.model = model

    def get_year(self):
        return self.year

    def set_year(self, year):
        self.year = year

    def get_manufacturer(self):
        return self.manufacturer

    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    def get_engine_capacity(self):
        return self.engine_capacity

    def set_engine_capacity(self, engine_capacity):
        self.engine_capacity = engine_capacity

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price


# Příklad použití třídy
auto = Car("Octavia", 2020, "Škoda", 1.6, "modrá", 500000)

# Výstup dat
print(auto.get_data())


print(auto.get_model())
print(auto.get_year())
print(auto.get_engine_capacity())
print(auto.get_color())
print(auto.get_price())
