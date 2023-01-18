class shape:
    def getArea(self): return self._area
    def getPerimeter(self): return self._perimeter
    def __str__(self): return "Perimeter: {0}, area: {1}".format(self._perimeter, self._area)

class circle(shape):
    def __init__(self,rad):
        self._area = (rad**2)*3.1415
        self._perimeter = 2*rad*3.1415

class equi_triangle(shape):
    def __init__(self,side):
        self._area = side**2*((3**0.5)/4)
        self._perimeter = 3*side

class rectangle(shape):
    def __init__(self,b,h):
        self._area = b*h
        self._perimeter = (b+h)*2

class square(rectangle):
    def __init__(self,side):
        self._area = side**2
        self._perimeter = 4*side

class pentagon(shape):
    def __init__(self,side):
        self._area = (side**2)*1.72
        self._perimeter = 5*side

class exagon(shape):
    def __init__(self,side):
        self._area = (side**2)*2.598
        self._perimeter = 6*side

class geomIter:
    def __iter__(self,l):
        self._l = sorted([x.getArea() for x in l], reverse=True)
        return self

    def __next__(self):
        first = self.l[0]
        self.l = self.l[1:]
        return first
