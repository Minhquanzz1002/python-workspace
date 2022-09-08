class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_area(self):
        result = self.length * self.width
        return result

    def calculate_perimeter(self):
        result = (self.length * self.width) * 2
        return result

    def display(self):
        print(f'Length: {self.length}, Width: {self.width}, Area: {self.calculate_area()}, Perimeter: {self.calculate_perimeter()}')
