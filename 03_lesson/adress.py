class Adress:
    def __init__(self, index, city, street, house, app):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.app = app

        def __str__(self):
            return (f"{self.index}, {self.city}, {self.street},"
                    f"{self.house}, {self.app}")
