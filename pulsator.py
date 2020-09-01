# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions


from blackhole import Black_Hole


class Pulsator(Black_Hole):
    counter=30
    
    def __init__(self,x,y):
        Black_Hole.__init__(self,x,y)
        self._count=0
    
    def update(self,selected):
        self._count+=1
        
        if len(selected)==0:
            
            Pulsator.counter-=1
            if Pulsator.counter==0:
                self.radius-=0.5
                Pulsator.counter=30
        else:
            if len(Black_Hole.update(self,selected))!=0:
                Pulsator.counter=30
                self.radius+=0.5
            else:
                Pulsator.counter-=1
                if Pulsator.counter==0:
                    self.radius-=0.5
                    Pulsator.counter=30
            
        if self.radius==0 or self._count==600:
            temp=Black_Hole.update(self,selected)
            temp.add(self)
            return temp
        
        return Black_Hole.update(self,selected)
    
    def display(self,canvas):
        canvas.create_oval(self._x-self.radius,self._y-self.radius,
                           self._x+self.radius,self._y+self.radius,
                           fill='black')
       