# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


#from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random


class Floater(Prey):
    radius = 5
    
    def __init__(self,x,y):
        Prey.randomize_angle(self)
        
        Prey.__init__(self,x,y,10,10,Prey.get_angle(self),5)
        
    
    def update(self):
        random_percent=random()
        while random_percent<=0.3:
            
            if self.get_speed()+0.5<=7 and self.get_speed()-0.5>=3:
                self._speed+=+-random()/2
                self._angle+=+-random()/2
            self.move()
            self.wall_bounce()
            random_percent=random()
        self.move()
        self.wall_bounce()
            
        
        
    def display(self,canvas):
        canvas.create_oval(self._x-Floater.radius,self._y-Floater.radius,
                           self._x+Floater.radius,self._y+Floater.radius,
                           fill='red')
