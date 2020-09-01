# Hunter is derived from the Mobile_Simulton/Pulsator classes: it updates
#   like a Pulsator, but it also moves (either in a straight line
#   or in pursuit of Prey), and displays as a Pulsator.


from prey import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2


class Hunter(Pulsator,Mobile_Simulton):
    
    dist=200
    
    def __init__(self,x,y):
        Pulsator.__init__(self,x,y)
        self.randomize_angle()
        self.get_angle()
        self._speed=5

       
    def update(self,selected):
        
        self.wall_bounce()
        self.move()
        temp=[]
        if len(selected)!=0:
            for s in selected:
                if self.distance(s.get_location()) <=Hunter.dist:
                    temp.append(s)
        
        if len(temp)!=0:
            x=sorted(temp,key=lambda x:self.distance(x.get_location()))
            dx=x[0].get_location()[0]-self.get_location()[0]
            dy=x[0].get_location()[1]-self.get_location()[1]
            self.set_angle(atan2(dy,dx))
            self.get_angle()

        return Pulsator.update(self,selected)
        
