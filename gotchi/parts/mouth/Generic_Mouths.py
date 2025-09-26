from ...general_tags import *

class Mouth():
    # generic mouth.
    def __init__(self, canvas, tag, center_x, center_y, width, height_offset):
        self.canvas = canvas
        self.x0 = center_x - width / 2
        self.y0 = center_y + height_offset
        self.x1 = center_x + width / 2
        self.y1 = self.y0 + 15 # Mouth height
        self.tag = tag 
        self.mouth = []

    def _draw_neutral(self):
        self.mouth.append(self.canvas.create_arc(
                self.x0, self.y0, self.x1, self.y1, 
                start=180, extent=180, 
                style="arc", width=3, 
                outline='black',
                tags = (self.tag,MOUTH)
            )
        )
    
    def draw_open(self):
        #self.mouth.append(
        self.canvas.create_oval(
                self.x0, self.y0, self.x1, self.y1,
                fill="black",
                outline="black",
                state="hidden",
                tags=(self.tag,MOUTH_OPEN)
            )
        #)

        #self.canvas.itemconfig(MOUTH_OPEN,state='hidden')

    def get_ids(self):
        self._draw_neutral()
        #self.draw_open()
        return self.mouth



