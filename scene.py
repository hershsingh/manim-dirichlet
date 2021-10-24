#!/bin/python
###

import numpy as np
import scipy as sp
import pandas as pd
from matplotlib import pyplot as plt

import random
from manim import *


class BezierCurve:
    def __init__(self, x1, dx1, x2, dx2):
        self.points = [x1, x2]
        self.d_handles = [[dx1, -dx2]]
        self.handles = [[x1 + dx1, x2 - dx2]]

    def get_length(self):
        return len(self.points)
        
    def add_point(self, x, dx):
        # self.points += [x]
        # self.d_handles += [[ -self.d_handles[-1][1], dx]]
        # self.handles += [[ -self.handles[-1][1], x+dx]]

        x_last = self.points[-1]
        d_handles_last = self.d_handles[-1][1]
        self.points += [x]
        self.d_handles += [[ -d_handles_last, -dx]]
        self.handles += [[ x_last - d_handles_last, self.points[-1] - dx]]

    def add_point_delta(self, x, dx):
        x_last = self.points[-1]
        d_handles_last = self.d_handles[-1][1]
        self.points += [x_last + x]
        self.d_handles += [[ -d_handles_last, -dx]]
        self.handles += [[ x_last - d_handles_last, self.points[-1] - dx]]

    def get_bezier_points(self, i):
        return [ self.points[i], self.handles[i][0], self.handles[i][1], self.points[i+1] ]

    def get_bezier(self, i):
        return CubicBezier(*self.get_bezier_points(i))

    def get_handles(self,i):

        d1 = Dot(point=self.points[i]).set_color(BLUE)
        d2 = Dot(point=self.points[i+1]).set_color(BLUE)

        # d1b = Dot(point=self.handles[i][0]).set_color(RED).
        # d2b = Dot(point=self.handles[i][-1]).set_color(RED)

        l1 = Arrow(self.points[i], self.handles[i][0], stroke_width=10.0, tip_shape=ArrowSquareTip, max_stroke_width_to_length_ratio=1)
        l2 = Arrow(self.points[i+1], self.handles[i][-1], stroke_width=10.0, tip_shape=ArrowSquareTip, max_stroke_width_to_length_ratio=1)

        l1.set_color(RED)
        l2.set_color(RED)

        return d1, l1, d2, l2

class Example(Scene):
    def construct(self):
        # vertices =[
        #     np.array([0,0, 0]),
        #     np.array([0 ,0 ,0]),
        #     np.array([4,1,0]),
        #     np.array([2 ,0 ,0])
        # ]

        # vertices =[
        #     np.array([-1]),
        #     np.array([0]),
        #     np.array([-4]),
        #     np.array([2])
        # ]


        # circle = Circle()  # create a circle
        # circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        # self.play(Create(circle))  # show the circle on screen

        # cubicBezier = CubicBezier(*vertices)
        # # self.play(Create(cubicBezier))

        # p1 = np.array([-3, 1, 0])
        # p1b = p1 + [1, 0, 0]
        # d1 = Dot(point=p1).set_color(BLUE)
        # l1 = Line(p1, p1b)
        # p2 = np.array([3, -1, 0])
        # p2b = p2 - [1, 0, 0]
        # d2 = Dot(point=p2).set_color(RED)
        # l2 = Line(p2, p2b)
        # bezier = CubicBezier(p1b, p1b + 2*RIGHT + 2*UP, p2b - 3 * RIGHT, p2b)
        # self.add(l1, d1, l2, d2, bezier)
        # self.add(bezier)
        # self.add(bezier)

        # points = [p1]
        # points += [points[-1] + 2*RIGHT+2*UP]
        # points += [points[-1] + 1*RIGHT]

        axes = Axes(
            x_range=[-2, 10, 1],
            y_range=[-2, 10, 1],
            # x_length=10,
            axis_config={"color": GREEN},
            # x_axis_config={
            #     "numbers_to_include": np.arange(-10, 10.01, 2),
            #     "numbers_with_elongated_ticks": np.arange(-10, 10.01, 2),
            # },
            tips=False,
        )
        # axes_labels = axes.get_axis_labels()
        # sin_graph = axes.get_graph(lambda x: np.sin(x), color=BLUE)
        # cos_graph = axes.get_graph(lambda x: np.cos(x), color=RED)

        # sin_label = axes.get_graph_label(
        #     sin_graph, "\\sin(x)", x_val=-10, direction=UP / 2
        # )
        # cos_label = axes.get_graph_label(cos_graph, label="\\cos(x)")

        # vert_line = axes.get_vertical_line(
        #     axes.i2gp(TAU, cos_graph), color=YELLOW, line_func=Line
        # )
        # line_label = axes.get_graph_label(
        #     cos_graph, "x=2\pi", x_val=TAU, direction=UR, color=WHITE
        # )

        plot = VGroup(axes)
        # labels = VGroup(axes_labels, sin_label, cos_label, line_label)

        grid = NumberPlane((-2, 10), (-2, 10))
        # self.add(grid)

        # self.wait()

        # p1 = ORIGIN

        # points = [p1, p1 + 2*RIGHT+2*UP]
        # handles = [[2*UP + RIGHT, -RIGHT - UP]]

        # points += [points[-1] + 1*RIGHT]
        # handles += [[-handles[-1][1], -RIGHT - UP]]

        # points += [points[-1] + 1*RIGHT]
        # handles += [[-handles[-1][1], -RIGHT - UP]]

        # # handles += [[2*UP + RIGHT, 0*LEFT]]
        self.x = 1

        num_points = 2


        def get_new_point():
            sign = random.choice([-1,1])
            if random.randint(0,1) == 0:
                return [sign, random.random(), 0.0]
            else:
                return [random.random(), sign, 0.0]

        # k = 0
        # N = 10
        origin = [1.,1.,0.]
        def point_generator(N=10):
            k = 0
            r = 3
            first = []
            while k <= N:

                if k==N:
                    yield first

                x = origin[0] + r*(np.cos(k*2*np.pi/N))
                y = origin[1] + r/2*np.sin(k*2*np.pi/N)

                noise = np.array([random.random(), random.random(), 0.0])
                noise = 0.2*(2*noise - 1)

                dd = random.random()*0.5 + 0.5
                dx = -dd*np.sin(k*2*np.pi/N)
                dy =  dd/2*np.cos(k*2*np.pi/N)

                p = np.array([x,y,0.0])+ noise
                dp = np.array([dx, dy, 0.0])
                if k==0:
                    first = [p, dp]

                k += 1
                yield np.array([x,y,0.0])+ noise, np.array([dx, dy, 0.0])
        N = 10
        pts = point_generator(N=N)
        def get_new_point():
            return next(pts)

        # print("points")
        # print(next(pts))
        # print(next(pts))
        # print(next(pts))
        # print(next(pts))
        # print(next(pts))

        # return

        def get_dx():
            xx= np.array([1.0, 0.3*random.random(), 0.0])
            # return 0.4 * xx/sum(xx**2)
            return 0.4 * xx/sum(xx**2)

        # dx1 = RIGHT + UP
        # last_dx = dx1 + get_dx()
        # last_dx = 
        # bez = BezierCurve(ORIGIN, dx1, p1 + get_new_point(), last_dx )
        x, dx = get_new_point()
        x2, dx2 = get_new_point()
        bez = BezierCurve(x, dx, x2, dx2)
        # print(dx1, last_dx)

        # bez.add_point_delta(RIGHT+UP, 0.5*(RIGHT+UP))
        for i in range(N-1):
            # last_dx += get_dx()
            x,dx = get_new_point()
            # print(i, pt)
            bez.add_point(x, dx)

        # last_dx += get_dx()
        # bez.add_point_delta(get_new_point(), get_dx())

        self.bez = bez
        # grp = VGroup([bez.get_bezier(i) for i in range(N)])
        # self.play(Create(grp))
        # self.play(Create(*[bez.get_bezier(i) for i in range(N)]))

        self.bl = [bez.get_bezier(i) for i in range(N)]
        # self.play(Create(self.bl[0]), Create(self.bl[1]))

        b = self.bl[0]
        b.add(*self.bl[1:])

        grp = VGroup(*self.bl)

        self.play(FadeIn(grid))
        self.play(Create(plot), run_time=2)
        # self.play(Create(grid))
        self.play(Create(grp), run_time=3, rate_func=rate_functions.linear)

        # Line
        self.wait(1)

        # for i in range(bez.get_length()-1):
        # # for i in range(1):
        #     # self.add(bez.get_bezier(i))
        #     # self.add(*bez.get_handles(i))

        #     self.play(Create((bez.get_bezier(i))))
        #     # self.add(*bez.get_handles(i))
        #     # self.play(bez)  # show the circle on screen

# s = Example()
# s.construct()

# print("adsd")

###
