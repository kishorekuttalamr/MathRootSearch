import numpy as np

def secant_method(equation, x0, x1, tolerance=1e-5, max_iterations=100):
    
    print(f"Iteration    x(n)       x(n-1)       x(n+1)       f(x(n+1))")
    print("-" * 60)
    
    for i in range(max_iterations):
        f_x0 = equation(x0)
        f_x1 = equation(x1)

        if abs(f_x1) < tolerance:
            return x1

        x2 = x1 - (f_x1 * (x1 - x0)) / (f_x1 - f_x0)

        print(f"{i+1:4d}     {x1:.6f}     {x0:.6f}     {x2:.6f}     {equation(x2):.6f}")

        if abs(x2 - x1) < tolerance:
            return x2

        x0, x1 = x1, x2

    raise Exception("Secant method did not converge within the maximum number of iterations.")


equation = lambda x: x+ np.exp(x)


x0 = 1
x1 = 0


root = secant_method(equation, x0, x1)


print("\nApproximate root:", round(root, 5))
