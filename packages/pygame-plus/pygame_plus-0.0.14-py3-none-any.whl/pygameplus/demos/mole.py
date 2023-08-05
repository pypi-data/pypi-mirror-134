
from importlib import resources
from pygameplus import *
from random import *

def main ():
    # Creating a screen
    screen = Screen(640, 360, "Whack-A-Mole")
    screen.background_color = "lightgreen"
    screen.open()
    
    # Function that moves the mole to a random location 
    # on the screen
    def move_mole ():
        mole.x = randint(-320, 320)
        mole.y = randint(-180, 180)
    
    # Create a mole sprite
    with resources.path("pygameplus.demos.img", "mole.png") as image_path:
        mole_image = load_picture(image_path)
    mole = Sprite(mole_image)
    mole.scale_factor = 0.2
    move_mole()
    screen.add(mole)
    
    # Start a timer that moves the mole every 2 seconds
    screen.on_timer(move_mole, 2000, repeat=True)
    
    # Create a mallet sprite
    with resources.path("pygameplus.demos.img", "mallet.png") as image_path:
        mallet_image = load_picture(image_path)
    mallet = Sprite(mallet_image)
    mallet.rotates = True
    mallet.scale_factor = 0.4
    screen.add(mallet)
    
    def hit ():
        mallet.turn_left(60)
    
    def release ():
        mallet.turn_right(60)
    
    def move_mallet (x, y):
        mallet.x = x + 10
        mallet.y = y + 30
    
    screen.on_click(hit)
    screen.on_release(release)
    screen.on_mouse_move(move_mallet)
    
    # Event loop
    start_event_loop()


# call the "main" function if running this script
if __name__ == "__main__":
    main()