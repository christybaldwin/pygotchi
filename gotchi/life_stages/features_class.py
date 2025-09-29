from ..parts.eyes.Generic_Eyes import Eyes
from ..parts.mouth.Generic_Mouths import Mouth
import random

class Features:
    # Defines the specific features for an adult.
    def __init__(self, canvas, center_x, center_y, body_size, tag, eyes_x_y_rad, mouth_x_y):

        #define specific body style features unique to this gotchi
        self.color = random.choice(["steelblue", "firebrick", "seagreen"])
        self.canvas = canvas
        self.center_x = center_x
        self.center_y = center_y
        self.body_size = body_size
        self.tag = tag
        self.eyes_x_y_rad = eyes_x_y_rad
        self.mouth_x_y = mouth_x_y
        # Coordinates for a triangle body
        #x0 = center_x - body_size / 2
        #y1 = center_y + body_size / 2
        #top_x = center_x
        #y0 = center_y - body_size / 2
        #x1 = center_x + body_size / 2
        #self.points = [x0, y1, top_x, y0, x1, y1]
        self.body_id = None # place holder



        # use universal or modular eyes / mouth 
        # each item is list item

    def draw_eyes(self):
        self.eyes = Eyes(
                        self.canvas, self.tag, self.center_x, self.center_y, 
                        x_offset=self.body_size/self.eyes_x_y_rad[0], y_offset=self.body_size/self.eyes_x_y_rad[1], radius=self.eyes_x_y_rad[2]
                    )

        self.eyes_ids = self._get_eyes_ids()


    def draw_mouth(self):
        self.mouth = Mouth( 
                        self.canvas, self.tag, self.center_x, self.center_y,  
                        width=self.body_size/self.mouth_x_y[0], height_offset=self.body_size/self.mouth_x_y[1]
                    )                                                           
        self.mouth_ids = self._get_mouth_ids()
    

    # returns list of concatinated lists
    def get_all_feature_ids(self):
        return self.body_id + self.eyes.get_ids() + self.mouth.get_ids()
    
    def get_body_id(self):
        return self.body_id

    def _get_eyes_ids(self):
        return self.eyes.get_ids()
 
    def _get_mouth_ids(self):
        return self.mouth.get_ids()
