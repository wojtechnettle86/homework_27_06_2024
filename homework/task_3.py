class Stadium:
    def __init__(self, name, opening_date, country, city, capacity):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def set_data(self, name, opening_date, country, city, capacity):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def get_data(self):
        return {
            'name': self.name,
            'opening_date': self.opening_date,
            'country': self.country,
            'city': self.city,
            'capacity': self.capacity
        }

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_opening_date(self):
        return self.opening_date

    def set_opening_date(self, opening_date):
        self.opening_date = opening_date

    def get_country(self):
        return self.country

    def set_country(self, country):
        self.country = country

    def get_city(self):
        return self.city

    def set_city(self, city):
        self.city = city

    def get_capacity(self):
        return self.capacity

    def set_capacity(self, capacity):
        self.capacity = capacity


stadion = Stadium("Wembley", "1923-04-28", "Velká Británie", "Londýn", 90000)

print(stadion.get_data())

print(stadion.get_name())
print(stadion.get_opening_date())
print(stadion.get_country())
print(stadion.get_city())
print(stadion.get_capacity())
