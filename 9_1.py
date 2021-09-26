class TrafficLight:
    __color = 'red'

    def running(self, color):
        from time import sleep
        traffic_timer = {'red': 7, 'yellow': 2, 'green': 5}
        color_code = {'red': '31m', 'yellow': '33m', 'green': '32m'}
        timer = traffic_timer.get(color)
        if color == 'red' and self.__color != 'green':
            timer = False
        if color == 'yellow' and self.__color != 'red':
            timer = False
        if color == 'green' and self.__color != 'yellow':
            timer = False
        if not timer:
            print('Неверное значение цвета светофора')
            raise SystemExit
        self.__color = color
        # TrafficLight.__color = color
        print(f"\033[{color_code.get(color)}{color}\033[0m")
        sleep(traffic_timer.get(color))

    def get_color(self):
        return self.__color


light1 = TrafficLight()
light1.running('yellow')
light1.running('green')
light1.running('red')
light1.running('green')
