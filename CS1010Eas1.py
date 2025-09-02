# Task 1: absolute difference between two roots
# =============================================
from math import sqrt


def rootsCharacter(a, b, c):
    # Insert code and comments below
    # Input: the coefficient(a,b,c) of the quadratic equation
    # Output: 1/-1/0 indicating the positivity/negativity of the roots
    x1 = ((-b) + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    x2 = ((-b) - sqrt(b ** 2 - 4 * a * c)) / (2 * a)  # assign values of 2 roots to x1, x2
    return 1 if (x1 > 0 and x2 > 0) else -1 if (x1 < 0 and x2 < 0) else 0
    # return 1 when both positive; -1 when both negative; 0 in other cases


# Task 2: polygon area
# ====================
from math import *


def areaPoly(n, d):
    # Insert code and comments below
    # Input: n(number of sides), d(length of each side)
    # Output: polygon area
    perimeter = n * d  # calculate the perimeter
    apothem = d / (2 * tan(pi / n))  # calculate the apothem
    return perimeter * apothem / 2  # calculate the area of polygon


def polySide(n, area):
    # Insert code and comments below
    # Input: number of sides(n), polygon area(area)
    # Output: length of one side
    return sqrt(4 * tan(pi / n) * area / n)  # derive d from area and return d


# Task 3: Area of a circle with an inscribed square
# =================================================
from math import pi


def find_circumcircle_area(sq_side):
    # Insert code and comments below
    # Input: length of the inscribed square side
    # Output: area of the circumcircle
    return pi * sq_side ** 2 / 2  # return the area


# Task 4: Gradient of a function at a point
# =========================================
def derivative(f):
    # Insert code and comments below
    # input: function(f)
    # Output: a function calculating the gradient of f(g)
    def g(x):
        return (f(x + 1e-5) - f(x)) / 1e-5  # calculate the derivative of f

    return g  # return the derivative-calculating function for f





