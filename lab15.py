from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * (self.radius ** 2)

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Circle) and self.radius == other.radius

    def __lt__(self, other: "Circle") -> bool:
        return self.radius < other.radius

    def __str__(self) -> str:
        return f"Circle(radius={self.radius})"


class Vector:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __abs__(self) -> float:
        return math.hypot(self.x, self.y)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Vector) and self.x == other.x and self.y == other.y

    def __lt__(self, other: "Vector") -> bool:
        return abs(self) < abs(other)

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"


def main():
    v1 = Vector(3, 4)
    v2 = Vector(2, 1)

    print("Vector 1:", v1)
    print("Vector 2:", v2)
    print("Vector addition :", v1 + v2)
    print("Vector magnitude:", abs(v1))
    print("v1 == v2:", v1 == v2)
    print("v1 < v2 :", v1 < v2)

    c1 = Circle(5)
    c2 = Circle(7)
    print("\nCircle 1:", c1)
    print("Area     :", round(c1.area(), 4))
    print("Perimeter:", round(c1.perimeter(), 4))
    print("c1 == c2 :", c1 == c2)
    print("c1 < c2  :", c1 < c2)


if __name__ == "__main__":
    main()
