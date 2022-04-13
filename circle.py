from math import pi,sqrt

class Circle:
    def __init__ (self, radius = None, diameter = None):

        if radius is None and diameter is None:
            raise ValueError('at least one element between radius and diameter must be defined')
        elif diameter is not None and radius is not None:
            if type(radius) is not str and type(diameter)is not str:
                if str(radius).startswith('-') or str(diameter).startswith('-'):
                    raise ValueError('parameters must be positive')
                if(diameter!=radius*2):
                    raise ValueError('Radius value: {radius} and diameter value: {diameter} are incompatible')
            else:
                raise TypeError('Radius value and diameter value must be a number')

        if radius is not None:
            self.radius=radius
            self.diameter=radius*2
            self.area=pi*radius**2
            self.circumference=self.diameter*pi
            
        else:
            self.diameter=diameter
            self.radius=diameter/2
            self.area=pi*(diameter/2)**2
            self.circumference=diameter*pi

        
    def print(self):
        print(f'Area: {round(self.area,4)} - Circumference: {round(self.circumference,4)} - Radius: {round(self.radius,4)} - Diameter: {round(self.diameter,4)}')

    def __str__(self):
        return f'Area: {round(self.area,4)} - Circumference: {round(self.circumference,4)} - Radius: {round(self.radius,4)} - Diameter: {round(self.diameter,4)}'

    def __add__(self, other):
        return Circle(radius = sqrt((self.area + other.area)/pi))

    def __lt__(self, other) :
        return True if self.area < other.area else False
    
    def __le__(self, other) :
        return True if self.area <= other.area else False
    
    def __gt__(self, other) :
        return True if self.area > other.area else False

    def __ge__(self, other) :
        return True if self.area >= other.area else False

    def __eq__(self, other) :
        return True if self.area == other.area else False
        