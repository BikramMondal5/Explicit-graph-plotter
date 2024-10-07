import numpy as np

import matplotlib.pyplot as plt

def plot_equation(equation, x_range=(-10, 10)):
    """
    Plots the graph of a given equation.

    Parameters:
    equation (str): The equation as a string, where 'x' is the variable.
    x_range (tuple): The range of x values to plot.
    """
    x = np.linspace(x_range[0], x_range[1], 400)
    y = eval(equation)

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=f'y = {equation}')
    plt.title('Graph of the Equation')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    plt.legend()
    plt.show()

equation = "np.tan(x)"
plot_equation(equation)
