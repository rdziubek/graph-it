import numpy as np
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider

from polynomial import Polynomial
from triangle import Triangle


def draw(master_point):
    # Dataset setup
    x = np.linspace(-5, 5, 101)

    # Plot formatting
    fig, ax = plt.subplots()

    ax.set_xlim([-4, 4])
    ax.set_ylim([-1, 4])

    # Data rendering
    ax.plot(x, Polynomial(x).value)

    ax.plot(*Triangle(Polynomial(x)).c.value, 'bo')

    slave_point_reference, = ax.plot(-master_point.x, master_point.y, 'bo')
    master_point_reference, = ax.plot(*master_point.value, 'bo')

    ax_slider = plt.axes([0.25, 0, 0.65, 0.03])
    point_a_argument = Slider(ax_slider, 'argument of A', 0, 10, valinit=0)

    def update(val):
        new_triangle = Triangle(Polynomial(point_a_argument.val))
        master_point_reference.set_ydata(new_triangle.polynomial.value)
        master_point_reference.set_xdata(new_triangle.a.x)
        slave_point_reference.set_ydata(new_triangle.polynomial.value)
        slave_point_reference.set_xdata(new_triangle.b.x)

        print(f'{new_triangle.to_string()}')
        print(f'Current area: {new_triangle.get_area()}')

        fig.canvas.draw_idle()

    point_a_argument.on_changed(update)

    plt.show()


x_optimal = 1
triangle = Triangle(Polynomial(x_optimal))

draw(triangle.a)
