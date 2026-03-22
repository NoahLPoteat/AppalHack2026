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
scene_controller: scene_handler.scene_handler = scene_handler.scene_handler()
clock = pygame.time.Clock()
running = True
handled: bool = False


logger.push_log("Initiation finished, beginning game loop")

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      logger.push_log("Closing sequence initiated, game will close at end of frame", False)
      running = False
    if event.type == pygame.MOUSEBUTTONUP:
      handled = False



  if pygame.mouse.get_pressed()[0] and not handled:
    scene_controller.advance_line()
    handled = pygame.mouse.get_pressed()[0]
    print(handled)
    print("HERE")


  
  # here we will reset the screen for the current frame
  window.reset_window()


  # SCENE CONTROL
  # here we will see if the current scene has changed, or if anything within the scene has changed
  # if anything has changed we will update the window with the setters
  #basically the all the game logic goes right here
  # print(scene_controller.line_num)
  print(len(scene_controller.get_lines()))
  window.set_dialogue(scene_controller.get_lines()[scene_controller.line_num]) #sets the current dialogue
  window.set_bg(scene_controller.get_bg_file_name())


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