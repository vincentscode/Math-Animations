import os
from manimlib.imports import *


class S1(GraphScene):
    CONFIG = {
        "x_min": -5,
        "x_max": 5,
        "y_min": -4,
        "y_max": 4,
        "graph_origin": ORIGIN,
        "function_color": WHITE,
        "axes_color": BLUE
    }

    def construct(self):
        # Make graph
        self.setup_axes(animate=True)
        func_graph = self.get_graph(self.x_squared, self.function_color)
        graph_lab = self.get_graph_label(func_graph, label="x^{2}")

        func_graph_2 = self.get_graph(self.x_cubed, self.function_color)
        graph_lab_2 = self.get_graph_label(func_graph_2, label="x^{3}")

        vert_line = self.get_vertical_line_to_graph(1, func_graph, color=YELLOW)

        x = self.coords_to_point(1, self.x_squared(1))
        y = self.coords_to_point(0, self.x_squared(1))
        horizontal_line = Line(x, y, color=YELLOW)

        point = Dot(self.coords_to_point(1, self.x_squared(1)))

        # Display graph
        self.play(ShowCreation(func_graph), Write(graph_lab))
        self.wait(1)
        self.play(ShowCreation(vert_line))
        self.play(ShowCreation(horizontal_line))
        self.add(point)
        self.wait(1)
        self.play(Transform(func_graph, func_graph_2), Transform(graph_lab, graph_lab_2))
        self.wait(2)

    @staticmethod
    def x_squared(x):
        return x ** 2

    @staticmethod
    def x_cubed(x):
        return x ** 3


if __name__ == '__main__':
    os.system("manim test.py S1 -p -s")
