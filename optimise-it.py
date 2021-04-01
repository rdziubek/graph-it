import numpy as np
from matplotlib import pyplot as plt, patches
from matplotlib.widgets import Slider

from point import Point
from rectangle import Rectangle

# Data setup
rectangle = Rectangle()

# Plot formatting
fig, ax = plt.subplots()

ax.set_xlim([0, Rectangle.BASE_PERIMETER / 2])
ax.set_ylim([0, Rectangle.BASE_PERIMETER / 2])


# Data rendering
def update_rendered_data(argument):
    rectangle.b = Point(argument)

    rectangle_commanding_anchor.set_xdata(rectangle.b.x)
    rectangle_commanding_anchor.set_ydata(rectangle.b.y)
    rectangle_drawn.set_width(rectangle.get_width())
    rectangle_drawn.set_height(rectangle.get_height())

    print(f'{rectangle.to_string()}\n'
          f'Current area: {rectangle.get_area()}')

    fig.canvas.draw_idle()


render_guide_domain = np.linspace(0, 18, 100)
ax.plot(render_guide_domain, -render_guide_domain + 18)

rectangle_commanding_anchor, = ax.plot(*rectangle.b.value, 'bo')
rectangle_drawn = patches.Rectangle(rectangle.a.value,
                                    rectangle.get_width(),
                                    rectangle.get_height(),
                                    linewidth=1, edgecolor='b', facecolor='none')
ax.add_patch(rectangle_drawn)

anchor_point_argument = Slider(plt.axes([0.25, 0, 0.65, 0.03]),
                               'Anchor argument',
                               0, Rectangle.BASE_PERIMETER / 2)
anchor_point_argument.on_changed(update_rendered_data)

plt.show()
