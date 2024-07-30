class CustomNumber:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        # Overload + operator to perform subtraction
        return self.value - other.value

    def __sub__(self, other):
        # Overload - operator to perform addition
        return self.value + other.value

    def __mul__(self, other):
        # Overload * operator to perform division
        return self.value / other.value

    def __truediv__(self, other):
        # Overload / operator to perform multiplication
        return self.value * other.value

    def __str__(self):
        return str(self.value)


# Example usage
if __name__ == "__main__":
    num1 = CustomNumber(10)
    num2 = CustomNumber(5)

    print(f"{num1} + {num2} = {num1 + num2}")  # Should perform subtraction
    print(f"{num1} - {num2} = {num1 - num2}")  # Should perform addition
    print(f"{num1} * {num2} = {num1 * num2}")  # Should perform division
    print(f"{num1} / {num2} = {num1 / num2}")  # Should perform multiplication
