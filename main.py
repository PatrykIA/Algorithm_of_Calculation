import math


def function(x):
    return 2 * math.exp(x) / (1 + math.exp(x - 1))


def rectangle_method(a, b, n):
    delta_x = (b - a) / n
    sum = 0

    for i in range(n):
        x_i = a + i * delta_x
        sum += function(x_i) * delta_x

    return sum


def trapezoid_method(a, b, n):
    delta_x = (b - a) / n
    sum = 0.5 * (function(a) + function(b)) * delta_x

    for i in range(1, n):
        x_i = a + i * delta_x
        sum += function(x_i) * delta_x

    return sum


def simpson_method(a, b, n):
    delta_x = (b - a) / n
    sum = (function(a) + function(b))

    for i in range(1, n):
        x_i = a + i * delta_x
        if i % 2 == 0:
            sum += 2 * function(x_i)
        else:
            sum += 4 * function(x_i)

    sum *= delta_x / 3
    return sum


def main():
    print("Program: Definite Integral Calculation")
    print()

    a = float(input("Enter the lower bound of the interval: "))
    b = float(input("Enter the upper bound of the interval: "))
    n = int(input("Enter the number of partitions: "))

    print("\nFunction formula: f(x) = 2 * (e^x / (1 + e^(x - 1)))")
    print("Number of partitions (n):", n)
    print("Interval bounds (a, b):", a, b)

    rectangle_result = rectangle_method(a, b, n)
    print("\nRectangle Method - Result:", rectangle_result)

    trapezoid_result = trapezoid_method(a, b, n)
    print("Trapezoid Method - Result:", trapezoid_result)

    simpson_result = simpson_method(a, b, n)
    print("Simpson's Method - Result:", simpson_result)


if __name__ == "__main__":
    main()
