from time import sleep
import tkinter as tk
from canvas_values import *
#from gotchi.gotchi_classes import Baby, Teen, Adult
from gotchi.gotchi_classes import Life_Stage
from food.food_classes import Cookie
from time import *

def main():
    
    # player sets name in terminal
    pygotchiname = input("What is your Pygotchi's name? ")

    # root tkinter object
    root = tk.Tk();
    root.title(f"{pygotchiname}'s World")

    # container canvas for main background, name, and nested gotchi_canvas
    main_canvas = tk.Canvas(root,width=CANVAS_WIDTH, height=CANVAS_HEIGHT,bg='lightblue')
    main_canvas.pack()

    gotchi_canvas = tk.Canvas(root, width=GOTCHI_BOX_WIDTH, height=GOTCHI_BOX_HEIGHT, bg='lightgray', highlightthickness=2, highlightbackground='black')
    main_canvas.create_window(GOTCHI_BOX_X, GOTCHI_BOX_Y, window=gotchi_canvas)

    # preload all the pigotchi life stages and hide them
    baby = Life_Stage(gotchi_canvas,"baby")
    teen = Life_Stage(gotchi_canvas,"teen")
    adult = Life_Stage(gotchi_canvas,"adult")
   
    # create food object and turn this instance into a button. NOTE: passing address of fucntion by NOT INCLUDING the '()'
    cookie_button = Cookie(main_canvas, gotchi_canvas, baby.eat_animation, BUTTON_1_X_LOCATION, BUTTON_1_Y_LOCATION)

    # Test text to display currnet life stage (default starting state is always baby)
    status_text = main_canvas.create_text(20,20, anchor="nw", font=("Arial", 30), fill='black',text=f"{pygotchiname} is a baby!")

    # gets current time for interval comparisons to be done for pygotchi life stages
    START_TIME = time()
    def game_loop():
        elapsed_time = time() - START_TIME
   
        # single var to denote which active gotchi to animate
        active_gotchi = baby
       
        # time checks for stages
        if elapsed_time < 20:
            active_gotchi = baby
            if(gotchi_canvas.itemcget(baby.parts[0],'state') == "hidden"):  # parts[0] (from the gotchi_class) is designed to always refer to the body of the gotchi
                baby.show()
                teen.hide()
                adult.hide()

        elif elapsed_time < 50:
            main_canvas.itemconfig(status_text, text=f"{pygotchiname} is now a teenager!")
            active_gotchi = teen
            if(gotchi_canvas.itemcget(teen.parts[0],'state') == "hidden"):
                baby.hide()
                teen.show()
                adult.hide()

        elif elapsed_time < 120:
            main_canvas.itemconfig(status_text, text=f"{pygotchiname} is an adult!")
            active_gotchi = adult
            if(gotchi_canvas.itemcget(adult.parts[0],'state') == "hidden"):
                baby.hide()
                teen.hide()
                adult.show()

        else:
            main_canvas.itemconfig(status_text, text=f"Great job raising {pygotchiname}!")
            return
        
        # update callback function based on currently active gotchi
        cookie_button.set_onClick_fun(active_gotchi.eat_animation)

        # run animaiton function for currently active_gotchi
        active_gotchi.move_animate()

        # update screen to reflect gotchi movment every 300 millieseconds
        root.after(300,game_loop)
            
    game_loop()
    root.mainloop()

if __name__ == '__main__':
    main()
