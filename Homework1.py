# ДЗ по теме "Наследование классов"
class Car:
    price = 1000000

    def __str__(self):
        return 'Model: {}, \nPrice: {}'.format(self.__class__.__name__,
                                    self.price)

    def horse_power(self):
        print(f'Количество лошадиных сил: 150')


class Nissan(Car):
    price = 1200000 #Переопределение свойства

    def horse_power(self): #Переопределение функции
        print(f'Количество лошадиных сил: 200')

class Kia(Car):
    price = 900000 #Переопределение свойства

    def horse_power(self): #Переопределение функции
        print(f'Количество лошадиных сил: 100')


nissan = Nissan()
print(nissan)
nissan.horse_power()
print()
kia = Kia()
print(kia)
kia.horse_power()