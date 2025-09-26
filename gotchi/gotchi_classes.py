from .life_stages.babies.Test_Baby import TestBabyFeatures
from .life_stages.teens.Test_Teen import TestTeenFeatures
from .life_stages.adults.Test_Adult import TestAdultFeatures
from gotchi.general_tags import *
import random
from time import *

# --- Base Class --- #
class Gotchi:
    """
    Grandparent class that handles the following logic:
        1) Animation / movement
        2) obtaining the root.canvas and dimensions
        3) holding parts[] list
    """
    def __init__(self,canvas):
        self.canvas = canvas
        self.parts = [] # used to hold id's of all parts of gotchi, this will allow for location manipulation later
        self.center_points = [] # used for holding the calculated starting points for each part of a gotchi to be used for location manipulation later
        self.tag = ""
        
        # get canvas dimensions
        self.canvas_width = int(self.canvas.cget("width"))
        self.canvas_height = int(self.canvas.cget("height"))

        # Velocity & direciton for movement animation
        self.dx = random.choice([-2,2])
        self.dy = random.choice([-2,2])

        # Universal center for gotchi body spawn
        self.center_x = self.canvas_width /2
        self.center_y = self.canvas_height /2

    
    def _reset_center(self):
        i = 0
        for part in self.parts:
            self.canvas.coords(part,*self.center_points[i])
            i += 1

    # used in main() function's game_loop() to disaplay gotchi movement 
    def move_animate(self):
        
        # guard clause to stop program if parts[] list is empty
        if not self.parts:
            return
        
        # calnvas.bbox will collect coordinate info for main body 
        # Notfe: assuming main body is first element added to list
        x0,y0,x1,y1 = self.canvas.bbox(self.parts[0])
        
        # check if any of main body's coordinates collide with edges of canvas
        if x0 <= 0 or x1 >= self.canvas_width:
            self.dx *= -1 # invert the direciton of dx upon collision  

        if y0 <= 0 or y1 >= self.canvas_height:
            self.dy *= -1 # invert the direciton of dy upon collision  

        # move ALL parts of gotchi as single unit (using tags)
        self.canvas.move(self.tag, self.dx, self. dy)

    
    def hide(self):
        #for part in self.parts:
        #   self.canvas.itemconfig(part,state='hidden')
        self.canvas.itemconfig(self.tag,state='hidden')

    def show(self):
        #for part in self.parts:
        #    self.canvas.itemconfig(part,state='normal')
        self.canvas.itemconfig(self.tag,state='normal')

    def add_happiness(self):
        print("clicked food, happiness increased")

    def _add_center_point(self,part):
        return self.canvas.coords(part)


# --- Life stage Subclass --- #
class Life_Stage(Gotchi):

    def __init__(self,canvas,type=""):
        super().__init__(canvas) # create instance of Gotchi (aka parent class) as part of current class

        if type == "baby":
            self.body_size = 95
            self.tag = "baby"

            # static features class for now, will update this in future to be modular in accepting another type of class file to represent different variants of baby gotchi
            self.features = TestBabyFeatures(self.canvas, self.center_x, self.center_y, self.body_size, self.tag)
        
        elif type == "teen":
            self.body_size = 130
            self.tag = "teen"
            self.features = TestTeenFeatures(self.canvas, self.center_x, self.center_y, self.body_size, self.tag)
        
        elif type == "adult":
            self.body_size = 190
            self.tag = "adult"
            self.features = TestAdultFeatures(self.canvas, self.center_x, self.center_y, self.body_size, self.tag)

        else:
            print("Error, no type was provided")
        

        # create parts list for the current instance
        for part in self.features.get_all_feature_ids():
            #self.add_part(part)
            self.parts.append(part)
            self.center_points.append(self._add_center_point(part))
        
        # static place holders for Ids of eyes and mouth canvas objects generated in features class 
        self.eyes_ids = self.features.eyes_ids
        self.mouth_ids = self.features.mouth_ids

        # after creation, start in hidden state 
        self.hide()
    
    # pass in the Cookie.draw & Cookie.bite_animation functions to add it to the gotchi canvas 
    def eat_animation(self):
        # start gotchi in neutral position and open mouth
        self._reset_center()

        if not self.canvas.find_withtag(MOUTH_OPEN):
            self._draw_open_mouth()
        
        else:
            # remove open mouth 
            self.canvas.delete(MOUTH_OPEN)

           
        # force additional screen update prior to main loop. Otherwise, function will run and finish without user ever seeing actions displayed on screen
        self.canvas.update()

        # sleep before bite to give appearance of normal paced biting animation
        sleep(.5)

    def _draw_open_mouth(self):
        self.features.mouth.draw_open()
        self.canvas.itemconfig(MOUTH_OPEN,state="normal")

