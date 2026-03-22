# TODO:
# Create a window that will display an image
# Detect user input, and propagate to input.py for handling it
# Next create a data structure (probably json/dict) to handle connecting scenes of the visual novel. These will point to a specific sceneData file (probably json again) which will handle bg image, char sprites, and dialogue (music if time)
#   Finally it will point to another scene within the initial dict (potentially split these but with scope of project it should be fine) Use the godot dialog json for example of this
# Build out jsonParser to parse these json files, and return them to pyVis
# finish todo 

import logger
import pygame
import scene
import scene_handler
from window import Window

logger.create_log_file()
# logger.push_log("Is this working too?")
# logger.push_log("YES IT IS", True)
pygame.init()

win_height: int = 640
win_width: int = 360



window = Window(win_height, win_width)
clock = pygame.time.Clock()
running = True


logger.push_log("Initiation finished, beginning game loop")

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      logger.push_log("Closing sequence initiated, game will close at end of frame", False)
      running = False

  # here we will reset the screen for the current frame
  window.reset_window()
  # here we will see if the current scene has changed, or if anything within the scene has changed
  # if anything has changed we will update the window with the setters
  #basically the all the game logic goes right here


  # here we will update the screen for the current frame now that we have set everything in 
 

  window.update()


  clock.tick(60) #sets game to 60 fps

# main loop here or something
# make the game here 


# #requires us to run the current_scene var 
# def swap_scene(sc_var: scene, next_scene: scene):
#   sc_var = next_scene

logger.push_log("Final frame finished. Closing Game...")
logger.close_logger()