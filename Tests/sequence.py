import os
import sys
from manimlib.imports import *


class S1(GraphScene, MovingCameraScene):
    x_max = 200
    x_steps = 10

    y_max = 5

    CONFIG = {
        "x_min": 0,
        "x_max": x_max,
        "x_tick_frequency": x_steps / 2,
        "x_labeled_nums": [x for x in range(0, x_max + 1, x_steps)],
        "x_axis_label": "$x$",
        "y_min": 0,
        "y_max": y_max,
        "y_tick_frequency": 1,
        "y_labeled_nums": [y for y in range(0, y_max + 1)],
        "y_axis_label": "$y$",
        "axes_color": BLUE,
        "graph_origin": 2.5 * DOWN + 4 * LEFT,
        "exclude_zero_label": True,
        "default_graph_colors": [BLUE, GREEN, YELLOW],
        "default_derivative_color": GREEN,
        "default_input_color": YELLOW,
        "default_riemann_start_color": BLUE,
        "default_riemann_end_color": GREEN,
        "area_opacity": 0.8,
        "num_rects": 50,
    }

    def setup(self):
        GraphScene.setup(self)
        MovingCameraScene.setup(self)

    def construct(self):
        self.setup_axes(animate=True)
        self.get_graph(self.graph_function)

        epsilon = 2
        tolerance = 0.1

        points = []
        for i in range(1, self.x_max+1):
            points.append(SmallDot(self.coords_to_point(i, self.graph_function(i))))

        self.wait(0.2)

        for point in points:
            self.add(point)
            self.wait(4 / len(points))

        self.wait(0.2)

        self.play(ShowCreation(Line(self.coords_to_point(0, epsilon), self.coords_to_point(self.x_max, epsilon), color=RED)))
        self.play(
            ShowCreation(DashedLine(self.coords_to_point(0, epsilon-tolerance), self.coords_to_point(self.x_max, epsilon-tolerance), color=RED)),
            ShowCreation(DashedLine(self.coords_to_point(0, epsilon+tolerance), self.coords_to_point(self.x_max, epsilon+tolerance), color=RED))
        )

        self.wait(3)

        self.play(
            self.camera_frame.scale, .5,
            self.camera_frame.move_to, points[100], LEFT
        )

        self.wait(3)

    @staticmethod
    def graph_function(n):
        return (2 * n - 1) / n


if __name__ == '__main__':
    if len(sys.argv[1:]) == 0:
        os.system("manim sequence.py S1 -p -l")
    else:
        os.system("manim sequence.py S1 " + ' '.join(sys.argv[1:]))
