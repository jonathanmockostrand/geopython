#class is a data container

from math import sqrt

class point():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def norm(self):
        return sqrt(self.x**2 + self.y**2)
        
    def __add__(self, other):
        return point(self.x + other.x, self.y + other.y)

    def __repr__(self):
        print 'point(%f, %f)' %  (self.x, self.y)
        
    def __str__(self):
        return '(%f, %f)' % (self.x, self.y)

p1 = point(1.0, 3.0)
p2 = point(3.0, 4.0)


print 'p1 = ', p1.x, p1.y
print 'p2 = ', p2.x, p2.y

print 'p1.norm() = ', p1.norm()
print 'p2.norm() = ', p2.norm()

print 'p1 + p2 = ', p1 +p2