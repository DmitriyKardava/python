class Car:
    speed = 0
    color = ''
    name = ''
    is_police = False

    def go(self, speed):
        self.speed = speed
        print(f'Машина {self.name} движется, скорость {speed}')

    def stop(self):
        self.speed = 0
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        print(f'Машина {self.name} повернула {direction}')

    def show_speed(self):
        print(f'Скорость {self.name}: {self.speed}')
        return self.speed


class TownCar(Car):
    def show_speed(self):
        print(f'Скорость {self.name}: {self.speed}')
        if self.speed > 60:
            print('Скорость превышена')
        return self.speed


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(f'Скорость {self.name}: {self.speed}')
        if self.speed > 60:
            print('Скорость превышена')
        return self.speed


class PoliceCar(Car):
    is_police = True


town_car = TownCar()
sport_car = SportCar()
work_car = WorkCar()
police_car = PoliceCar()

town_car.speed = 80
town_car.name = 'town car'
town_car.show_speed()
town_car.turn('на право')

sport_car.speed = 120
sport_car.name = 'sport car'
sport_car.stop()
sport_car.show_speed()

work_car.name = 'work car'
print(work_car.is_police)

police_car.name = 'police car'
print(police_car.is_police)