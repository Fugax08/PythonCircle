import pytest

from circle import Circle

circle1 = Circle(radius = 5)
circle2 = Circle(diameter = 6)
circle3 = Circle(diameter = 10)

def test_init_with_radius():
    assert circle1.diameter==10
    
def test_init_with_diameter():
    assert circle2.radius==3
    
def test_init_area():
    assert round(circle1.area,4)==78.5398

def test_print():
    string = "Area: 78.5398 - Circumference: 31.4159 - Radius: 5 - Diameter: 10"
    string2 = circle1.__str__()
    assert string2==string

def test_add():
    circle_sum = circle1 + circle2
    assert round(circle_sum.area,4)==106.8142
    
def test_greater():
    assert circle1>circle2
    
def test_lower_():
    assert circle2<circle1
    
def test_equal():
    assert circle1==circle3

def test_list_sort():
    circle4 = Circle(radius = 6)
    circle5 = Circle(radius = 4)
    circle_list = []
    circle_list.append(circle1)
    circle_list.append(circle2)
    circle_list.append(circle4)
    circle_list.append(circle5)
    circle_list.sort()
    assert circle_list[0] == circle2
    assert circle_list[1] == circle5
    assert circle_list[2] == circle1
    assert circle_list[3] == circle4
    