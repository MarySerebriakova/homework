import random

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._cords = [0, 0, 0]  # Координаты в пространстве
        self.speed = speed  # Скорость передвижения

    def move(self, dx, dy, dz):
        new_z = self._cords[2] + dz * self.speed
        if new_z < 0:
            print("It's too deep, I can't dive :(")
        else:
            self._cords[0] += dx * self.speed
            self._cords[1] += dy * self.speed
            self._cords[2] = new_z

    def get_cords(self):
        print(f"X: {self._cords[0]} Y: {self._cords[1]} Z: {self._cords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, I'm peaceful :)")
        else:
            print("Be careful, I'm attacking you 0_0")

    def speak(self):
        print(self.sound)

class Bird(Animal):
    beak = True  # Наличие клюва

    def lay_eggs(self):
        print(f"Here are(is) {random.randint(1, 4)} eggs for you")

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        dz = abs(dz)  # Делаем dz положительным
        self.move(0, 0, -dz)  # Ныряем, dx и dy равны 0
        self.speed /= 2  # Уменьшаем скорость в 2 раза

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    sound = "Click-click-click"

# Пример работы программы:
db = Duckbill(10)

print(db.live)        # True
print(db.beak)       # True
db.speak()           # Click-click-click
db.attack()          # Be careful, I'm attacking you 0_0
db.move(1, 2, 3)     # Перемещаемся
db.get_cords()       # X: 10 Y: 20 Z: 30
db.dive_in(6)        # Ныряем
db.get_cords()       # X: 10 Y: 20 Z: 0
db.lay_eggs()        # Откладываем яйца