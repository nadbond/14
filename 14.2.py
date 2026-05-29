class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating

    def describe_restaurant(self):
        print(f"Название: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")
        print(f"Рейтинг: {self.rating}")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors, location, working_hours):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
        self.location = location
        self.working_hours = working_hours

    def show_info(self):
        print(f"Кафе: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")
        print(f"Локация: {self.location}")
        print(f"Время работы: {self.working_hours}")

    def show_flavors(self):
        print("Сорта мороженого:")
        for flavor in self.flavors:
            print(flavor)

    def add_flavor(self, flavor):
        if flavor not in self.flavors:
            self.flavors.append(flavor)
            print(f"Сорт '{flavor}' добавлен.")
        else:
            print("Такой сорт уже существует.")

    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)
            print(f"Сорт '{flavor}' удалён.")
        else:
            print("Такого сорта нет.")

    def check_flavor(self, flavor):
        if flavor in self.flavors:
            print(f"Сорт '{flavor}' есть в наличии.")
        else:
            print(f"Сорт '{flavor}' отсутствует.")

    def stick_ice_cream(self):
        print("Мороженое на палочке доступно.")

    def soft_ice_cream(self):
        print("Мягкое мороженое доступно.")

    def waffle_ice_cream(self):
        print("Мороженое в вафельном рожке доступно.")

cafe = IceCreamStand(
    "ОтМороженное",
    "Кафе-мороженое",
    ["Шоколад", "Клубника", "Банан", "Бабл-гам", "Ваниль"],
    "Город Пупкин, Переулок Жопкин, дом 23",
    "10:00 - 19:00")

cafe.show_info()
print()
cafe.show_flavors()
print()
cafe.add_flavor("Мята")
cafe.remove_flavor("Ваниль")
print()
cafe.check_flavor("Шоколад")
cafe.check_flavor("Манго")
print()
cafe.stick_ice_cream()
cafe.soft_ice_cream()
cafe.waffle_ice_cream()