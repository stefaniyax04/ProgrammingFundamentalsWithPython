# Create a class Circle. In the __init__ method, the circle should only receive one parameter -
# its diameter. Create a class attribute called __pi that is equal to 3.14. The class should also
# have the following methods:
# · calculate_circumference() - returns the circumference of the circle
# · calculate_area() - returns the area of the circle
# · calculate_area_of_sector(angle) - gives the central angle in degrees, returns the area that fills the sector.


class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = diameter/2


    def calculate_circumference(self):
        return 2 * Circle.__pi * self.radius


    def calculate_area(self):
        return Circle.__pi * (self.radius ** 2)


    def calculate_area_of_sector(self, angle):
        return (angle / 360) * Circle.__pi * (self.radius ** 2)