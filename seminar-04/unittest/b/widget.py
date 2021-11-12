# Создадим класс, который будем тестировать

class Widget:

    def __init__(self, name, x=50, y=50):
        self.name = name
        self.x = x
        self.y = y

    def size(self):
        return self.x, self.y

    def resize(self, x_, y_):
        self.x, self.y = x_, y_
