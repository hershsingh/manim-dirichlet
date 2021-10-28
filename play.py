#!/bin/python
###

# from manim import *
import manim

class Example(manim.Scene):
    def construct(self):
        circle = manim.Circle()  # create a circle
        circle.set_fill(manim.PINK, opacity=0.5)  # set the color and transparency
        anim = manim.Create(circle) 
        self.play( anim )  # show the circle on screen

# class Complex:
#     def __init__(self, real, imag):
#         # print("Inside constructor")

#         self.real = real
#         self.imag = imag

#     def __repr__(self):
#         return "{:f} + i{:f}".format(self.real, self.imag)

#     def __add__(self, z):
#         real = self.real + z.real
#         imag = self.imag + z.imag

#         return Complex(real, imag)

# class ComplexUnit(Complex):
#     def __init__(self, real, imag):
#         super().__init__(real, imag)

#         self.norm = (self.real**2 + self.imag**2)**(0.5)
#         self.real /= self.norm
#         self.imag /= self.norm
#         self.norm = 1.0

#     def __add__(self, z):
#         real = self.real + z.real
#         imag = self.imag + z.imag

#         return ComplexUnit(real, imag)

# x = ComplexUnit(2.0, 3.0)
# y = ComplexUnit(2.0, 3.0)


    
# ###

# # Complex() =>
# # 1. Allocate memory for object "x" of type "Complex"
# # 2. Call the function: Complex.__init__(x)
    
# # x = Complex(1.0, 2.0)
# # y = Complex(1.0, 2.0)
# # x + y => x.__add__(y)
# # x + y => add(x,y) => add_int(x, y)

# # x + y => x.add(y)

# # add(x,y)
# # add(int, int) => add_int()
# # add(float, float) => add_float()
# # add(float, int) => add_float_int()
# # add(int, float) ..
# # add(str, str) ..












# # import random
# # import numpy as np
# # import scipy as sp
# # from matplotlib import pyplot as plt

# #         # vertices =[
# #         #     np.array([0,0, 0]),
# #         #     np.array([0 ,0 ,0]),
# #         #     np.array([4,1,0]),
# #         #     np.array([2 ,0 ,0])
# #         # ]

# #         # vertices =[
# #         #     np.array([-1]),
# #         #     np.array([0]),
# #         #     np.array([-4]),
# #         #     np.array([2])
# #         # ]


# #         # circle = Circle()  # create a circle
# #         # circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
# #         # self.play(Create(circle))  # show the circle on screen

# #         # cubicBezier = CubicBezier(*vertices)
# #         # # self.play(Create(cubicBezier))

# #         # p1 = np.array([-3, 1, 0])
# #         # p1b = p1 + [1, 0, 0]
# #         # d1 = Dot(point=p1).set_color(BLUE)
# #         # l1 = Line(p1, p1b)
# #         # p2 = np.array([3, -1, 0])
# #         # p2b = p2 - [1, 0, 0]
# #         # d2 = Dot(point=p2).set_color(RED)
# #         # l2 = Line(p2, p2b)
# #         # bezier = CubicBezier(p1b, p1b + 2*RIGHT + 2*UP, p2b - 3 * RIGHT, p2b)
# #         # self.add(l1, d1, l2, d2, bezier)
# #         # self.add(bezier)
# #         # self.add(bezier)

# #         # points = [p1]
# #         # points += [points[-1] + 2*RIGHT+2*UP]
# #         # points += [points[-1] + 1*RIGHT]

# #         axes = Axes(
# #             x_range=[-2, 10, 1],
# #             y_range=[-2, 10, 1],
# #             # x_length=10,
# #             axis_config={"color": GREEN},
# #             # x_axis_config={
# #             #     "numbers_to_include": np.arange(-10, 10.01, 2),
# #             #     "numbers_with_elongated_ticks": np.arange(-10, 10.01, 2),
# #             # },
# #             tips=False,
# #         )
# #         # axes_labels = axes.get_axis_labels()
# #         # sin_graph = axes.get_graph(lambda x: np.sin(x), color=BLUE)
# #         # cos_graph = axes.get_graph(lambda x: np.cos(x), color=RED)

# #         # sin_label = axes.get_graph_label(
# #         #     sin_graph, "\\sin(x)", x_val=-10, direction=UP / 2
# #         # )
# #         # cos_label = axes.get_graph_label(cos_graph, label="\\cos(x)")

# #         # vert_line = axes.get_vertical_line(
# #         #     axes.i2gp(TAU, cos_graph), color=YELLOW, line_func=Line
# #         # )
# #         # line_label = axes.get_graph_label(
# #         #     cos_graph, "x=2\pi", x_val=TAU, direction=UR, color=WHITE
# #         # )

# #         plot = VGroup(axes)
# #         # labels = VGroup(axes_labels, sin_label, cos_label, line_label)

# #         grid = NumberPlane((-2, 10), (-2, 10))
# #         # self.add(grid)

# #         # self.wait()

# #         # p1 = ORIGIN

# #         # points = [p1, p1 + 2*RIGHT+2*UP]
# #         # handles = [[2*UP + RIGHT, -RIGHT - UP]]

# #         # points += [points[-1] + 1*RIGHT]
# #         # handles += [[-handles[-1][1], -RIGHT - UP]]

# #         # points += [points[-1] + 1*RIGHT]
# #         # handles += [[-handles[-1][1], -RIGHT - UP]]

# #         # # handles += [[2*UP + RIGHT, 0*LEFT]]
# #         self.x = 1

# #         num_points = 2


# #         def get_new_point():
# #             sign = random.choice([-1,1])
# #             if random.randint(0,1) == 0:
# #                 return [sign, random.random(), 0.0]
# #             else:
# #                 return [random.random(), sign, 0.0]

# #         # k = 0
# #         # N = 10
# #         origin = [1.,1.,0.]
# #         def point_generator(N=10):
# #             k = 0
# #             r = 3
# #             first = []
# #             while k <= N:

# #                 if k==N:
# #                     yield first

# #                 x = origin[0] + r*(np.cos(k*2*np.pi/N))
# #                 y = origin[1] + r/2*np.sin(k*2*np.pi/N)

# #                 noise = np.array([random.random(), random.random(), 0.0])
# #                 noise = 0.2*(2*noise - 1)

# #                 dd = random.random()*0.5 + 0.5
# #                 dx = -dd*np.sin(k*2*np.pi/N)
# #                 dy =  dd/2*np.cos(k*2*np.pi/N)

# #                 p = np.array([x,y,0.0])+ noise
# #                 dp = np.array([dx, dy, 0.0])
# #                 if k==0:
# #                     first = [p, dp]

# #                 k += 1
# #                 yield np.array([x,y,0.0])+ noise, np.array([dx, dy, 0.0])
# #         N = 10
# #         pts = point_generator(N=N)
# #         def get_new_point():
# #             return next(pts)

# #         # print("points")
# #         # print(next(pts))
# #         # print(next(pts))
# #         # print(next(pts))
# #         # print(next(pts))
# #         # print(next(pts))

# #         # return

# #         def get_dx():
# #             xx= np.array([1.0, 0.3*random.random(), 0.0])
# #             # return 0.4 * xx/sum(xx**2)
# #             return 0.4 * xx/sum(xx**2)

# #         # dx1 = RIGHT + UP
# #         # last_dx = dx1 + get_dx()
# #         # last_dx = 
# #         # bez = BezierCurve(ORIGIN, dx1, p1 + get_new_point(), last_dx )
# #         x, dx = get_new_point()
# #         x2, dx2 = get_new_point()
# #         bez = BezierCurve(x, dx, x2, dx2)
# #         # print(dx1, last_dx)

# #         # bez.add_point_delta(RIGHT+UP, 0.5*(RIGHT+UP))
# #         for i in range(N-1):
# #             # last_dx += get_dx()
# #             x,dx = get_new_point()
# #             # print(i, pt)
# #             bez.add_point(x, dx)

# #         # last_dx += get_dx()
# #         # bez.add_point_delta(get_new_point(), get_dx())

# #         self.bez = bez
# #         # grp = VGroup([bez.get_bezier(i) for i in range(N)])
# #         # self.play(Create(grp))
# #         # self.play(Create(*[bez.get_bezier(i) for i in range(N)]))

# #         self.bl = [bez.get_bezier(i) for i in range(N)]
# #         # self.play(Create(self.bl[0]), Create(self.bl[1]))

# #         b = self.bl[0]
# #         b.add(*self.bl[1:])

# #         grp = VGroup(*self.bl)

# #         # self.play(FadeIn(grid))
# #         self.play(Create(plot), run_time=2)
# #         # self.play(Create(grid))
# #         self.play(Create(grp), run_time=3, rate_func=rate_functions.linear)

# #         grid_config = {
# #             # "axis_config": {
# #             #     "stroke_color": WHITE,
# #             #     "stroke_width": 2,
# #             #     "include_ticks": False,
# #             #     "include_tip": False,
# #             #     "line_to_number_buff": SMALL_BUFF,
# #             #     "label_direction": DR,
# #             #     "number_scale_val": 0.5,
# #             # },
# #             # "y_axis_config": {
# #             #     "label_direction": DR,
# #             # },
# #             "background_line_style": {
# #                 "stroke_color": BLUE_D,
# #                 "stroke_width": 2,
# #                 "stroke_opacity": 1,
# #             },
# #             # Defaults to a faded version of line_config
# #             # "faded_line_style": None,
# #             # "x_line_frequency": 1,
# #             # "y_line_frequency": 1,
# #             # "faded_line_ratio": 1,
# #             # "make_smooth_after_applying_functions": True,}
# #         }
        
# #         grid = NumberPlane((-2, 10), (-2, 10), **grid_config)

# #         self.play(FadeIn(grid))
# #         # self.add(grid)

# #         # Line
# #         self.wait(1)

# #         # for i in range(bez.get_length()-1):
# #         # # for i in range(1):
# #         #     # self.add(bez.get_bezier(i))
# #         #     # self.add(*bez.get_handles(i))

# #         #     self.play(Create((bez.get_bezier(i))))
# #         #     # self.add(*bez.get_handles(i))
# #         #     # self.play(bez)  # show the circle on screen

# # # s = Example()
# # # s.construct()

# # # print("adsd")

# # ##

# # p = np.array([3.0,2.1])

# # def check_int(p):
# #     """Return 0,1,2,3 depending on whether either of (x,y) is an integer"""
# #     return sum(np.isclose(p%1, 0)*[2,1])

# # def check_entry_exit(p, theta):
# #     """Whether a line is entering or exiting depends on the slope"""
# #     c = check_int(p)
# #     if c==1: # (x,y) y is integer. Intersects horizontal grid
# #         if theta>0 and theta<np.pi:
# #             return 0 # entry
# #         else:
# #             return 1 # exit
# #     elif c==2: # Intersects vertical grid
# #         if theta>PI/2 and theta < (3/2)*PI:
# #             return 0 # entry
# #         else:
# #             return 1 # exit
# #     else:
# #         return -1 # At a strange place
        
# # def get_next_bdy(p):
# #     # check whether we intersect vertical or horizontal grid
# #     c = check_int(p) 
# #     # choices = [[]]

# # print(check_int(p))

# # ###

# # n = 10
# # [1]*n + [-1]*n
