
# Black_Hole is derived from Simulton only: it updates by finding/removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey

class Black_Hole(Simulton):
    radius=10
    def __init__(self,x,y):
        Simulton.__init__(self,x,y,20,20)
        
    
    def update(self,selected):
        if selected!=set():
            temp=set()
            for s in selected:
                if self.__contains__(s):
                    temp.add(s)
            return temp
        else:
            return selected
        
                
    def display(self,canvas):
        canvas.create_oval(self._x-Black_Hole.radius,self._y-Black_Hole.radius,
                           self._x+Black_Hole.radius,self._y+Black_Hole.radius,
                           fill='black')
        
    def __contains__(self,object):
        if self.distance((object._x,object._y)) <=self.radius and isinstance(object, Prey):
            return True
        

        