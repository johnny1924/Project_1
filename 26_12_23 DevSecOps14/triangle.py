class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calc_area(self):
        area = 0.5 * self.base * self.height
        return area

# Example usage:
triangle_instance = Triangle(5, 8)
triangle_area = triangle_instance.calc_area()
print(f"The area of the triangle is: {triangle_area}")
