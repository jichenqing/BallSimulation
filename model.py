import controller, sys
import model   #strange, but we need a reference to this module to pass this module to update

from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter
from prey      import Prey
from special   import Special

# Global variables: declare them global in functions that assign to them: e.g., ... = or +=

simultons = set()
object = None
clearobjects = set()
running = False
cycle_count = 0


#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running, cycle_count, simultons
    running=False
    cycle_count=0
    simultons=set()

#start running the simulation
def start ():
    global running
    running=True
    

#stop running the simulation (freezing it)
def stop ():
    global running
    running=False


#tep just one update in the simulation
def step ():
    global running,cycle_count
    if running:
        running=False
    else:
        running=True
        update_all()
        running=False


#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global object
    object=kind


#add the kind of remembered object to the simulation (or remove all objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    
    global simultons,object,clearobjects
    
    if object!='Remove':
        try:
            simultons.add( eval(object)(x,y))
        except:
            pass
    else:
        for s in simultons:
            if s.distance((x,y))<=s.radius:
                clearobjects.add(s)

#add simulton s to the simulation
def add(s):
    global simultons
    simultons.add(s)
    

# remove simulton s from the simulation    
def remove(s):
    global simultons
    if s in simultons:
        simultons.remove(s)
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    new=set()
    for simulton in simultons:
        if p(simulton):
            new.add(simulton)
    return new


#call update for every simulton in the simulation
def update_all():
    global simultons,cycle_count
    
    if running:
        cycle_count+=1
        for simulton in simultons.copy():
            if isinstance(simulton, Black_Hole) or isinstance(simulton,Pulsator)or\
            isinstance(simulton,Hunter) or isinstance(simulton, Special):
                selected=find(lambda x:isinstance(x, Prey))
                simulton1=simulton.update(selected)
                if simulton1!=set():
                    clearobjects.update(simulton1)
                        
            else:
                simulton.update()
                
    if len(clearobjects)!=0:
        for object in clearobjects:
            remove(object)
        clearobjects.clear()     

#delete every simulton being simulated from the canvas; then call display for every
#  simulton being simulated to add it back to the canvas, possibly in a new location, to
#  animate it; also, update the progress label defined in the controller
def display_all():
    global simultons
    for s in controller.the_canvas.find_all():
        controller.the_canvas.delete(s)
    for simulton in simultons:
        simulton.display(controller.the_canvas)
    
    controller.the_progress.config(text=str(len(simultons))+" simultons/"+str(cycle_count)+" cycles")
    
    
