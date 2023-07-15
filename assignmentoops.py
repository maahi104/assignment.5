class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def sum_of_squares(self):
        return self.x**2 + self.y**2 + self.z**2
        

x = int(input("Enter x-coordinate: "))
y = int(input("Enter y-coordinate: "))
z = int(input("Enter z-coordinate: "))
object1 = Point(x, y, z)
print("Sum of squared numbers:", object1.sum_of_squares())
