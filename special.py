# The Special object is a Black_Hole that
# every time it eats a Prey, its color becomes red then becomes black again

from blackhole import Black_Hole
import controller

class Special(Black_Hole):
    eaten=0
    def __init__(self,x,y):
        Black_Hole.__init__(self,x,y)
    
    def update(self,selected):
        temp=Black_Hole.update(self,selected)
        if len(temp)!=0:
            Special.eaten+=len(temp)
        return temp
    
    def display(self,canvas):
        if Special.eaten!=0:
            for c in range(Special.eaten):
                canvas.create_oval(self._x-Black_Hole.radius,self._y-Black_Hole.radius,
                                   self._x+Black_Hole.radius,self._y+Black_Hole.radius,
                                   fill='red')
        else:
            Black_Hole.display(self,canvas)
        
        Special.eaten=0