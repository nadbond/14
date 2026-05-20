class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating

    def describe_restaurant(self):  # ← новый метод
        print(f"Название: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")
        print(f"Рейтинг: {self.rating}")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, rating=0):
        super().__init__(restaurant_name, cuisine_type, rating)
        self.flavors = ["Шоколад", "Клубника", "Банан", "Бабл-гам", "Ваниль"]

    def show_flavors(self):
        print("Сорта мороженого:")
        for flavor in self.flavors:
            print("-", flavor)

shop = IceCreamStand("ОтМороженное", "Кафе-мороженое", 10.0)
shop.describe_restaurant()
print()
shop.show_flavors()