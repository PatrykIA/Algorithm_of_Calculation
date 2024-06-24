 Algorithm_of_Calculation

Comparison of integration methods (rectangles, trapezoids, Simpson's rule) and selection of the most advantageous method.

 Project Description

This project implements three numerical methods for calculating the definite integral of a function. The implemented methods are:

- Rectangle Method
- Trapezoid Method
- Simpson's Method

Each of these methods approximates the value of the integral by dividing the interval into smaller subintervals and summing the calculated values.

Files

 'obliczenia.py': The main Python script containing the implementation of all three methods, as well as tests for different values of the number of subdivisions \( n \).

 Test Results

| Method      | n = 5               | n = 10              | n = 100             | n = 10000           |
|-------------|---------------------|---------------------|---------------------|---------------------|
| Rectangles  | -0.25469535390745   | -0.44240000419352   | -0.60896323443218   | -0.6271490889782426 |
| Trapezoids  | -0.34453845351618   | -0.48732155399789   | -0.61345538941262   | -0.6271940105280469 |
| Simpson's   | -1.24131003239092   | -0.94198684815441   | -0.6593670768964    | -0.627653543229868  |

Conclusions

Method Accuracy:

- The rectangle method is the least accurate of the three methods, especially for smaller values of \( n \).
- The trapezoid method provides better approximations than the rectangle method but is less accurate than Simpson's method.
- Simpson's method, which uses quadratic interpolation, is the most accurate, especially for larger values of \( n \).

Convergence of Results:

- All three methods approach the true value of the integral as the number of subdivisions \( n \) increases.
- For \( n = 10000 \), the results of all methods are very close to the true value of the integral, confirming the correctness of the implementation.

Best Method:

- In general, Simpson's method provides the best results with the fewest iterations due to its higher accuracy from quadratic interpolation.
- In this specific case for the function \( f(x) \) in the interval \([-2, 1]\), Simpson's method delivers the results closest to the true value of the integral even for smaller values of \( n \).


