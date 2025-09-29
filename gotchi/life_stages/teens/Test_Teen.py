# from ...parts.eyes.Generic_Eyes import Eyes
# from ...parts.mouth.Generic_Mouths import Mouth
# import random
from ..features_class import Features

class TestTeenFeatures(Features):
    # Defines the specific features for a teen.
    def __init__(self, canvas, center_x, center_y, body_size, tag):
        super().__init__(canvas,center_x,center_y,body_size,tag,[3.5,4,12],[2.5,6])
        
        #define specific body style features unique to this gotchi
        #color = random.choice(["steelblue","firebrick","seagreen"])
        x0 = center_x - body_size/2
        y0 = center_y - body_size/2
        x1 = center_x + body_size/2
        y1 = center_y + body_size/2

        points = [x0,y0,x1,y1]

        # creates single list item to ALLWAYS be appened first
        self.body_id = [canvas.create_rectangle(
                                    points, 
                                    fill=self.color, 
                                    outline='black', 
                                    width=2,
                                    tags = tag
                        )
        ]

        self.draw_eyes()
        self.draw_mouth()

       
        # use universal or modular eyes / mouth 
        # each item is list item
    #     self.eyes = Eyes(
    #                     canvas, tag, center_x, center_y, 
    #                     x_offset=body_size/3.5, y_offset=body_size/4, 
    #                     radius=12
    #                 )
    #     self.mouth = Mouth(
    #                     canvas, tag, center_x, center_y, 
    #                     width=body_size/2.5, 
    #                     height_offset=body_size/6
    #                 )
    #
    # # returns list of concatinated lists
    # def get_all_feature_ids(self):
    #     return self.body_id + self.eyes.get_ids() + self.mouth.get_ids()
    #

