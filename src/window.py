import pygame
import logger
import scene as Scene

class Window:
  bg_img: pygame.Surface = None

  #= load(textbox.png) or something like that
  text_box: pygame.Surface = pygame.image.load("Assets/gen/text_box.png") 
  text_box_pos = (40,216) #based on text box being 560x144
  
  cur_dialogue: Scene.dialogue = None
  cur_scene_name: str = ""
  chars = [] 

  def __init__(self, win_width: int, win_height: int):
        global screen 
        screen = pygame.display.set_mode((win_width, win_height))

  def update(self):
    
    #here we will layer the sprites to the screen using blit

    #first the background
    if self.bg_img == None:
        logger.push_log("Unable to find bg_img for scene "
                         + self.cur_scene_name + ", using placeholder", True)
        self.set_bg("placeholder.png")

    bg_pos = (0,0)
    screen.blit(self.bg_img, bg_pos)
    
    #Next any ui elements that need to be behind the player 
    # (save and load button)

    # (exit button)

    # (maybe: character love meter)


    #Then we need to render each character at their specified position
    if len(self.chars) == 1:
      char_pos = (192, 128) #centered for one character
      #char_surface = load_char_image(self.chars[0].get_sprite(emotion))
      #screen.blit(char_surface, char_pos)

    elif len(self.chars) == 2:
      char1_pos = (0,0) #calculate this at some point loser
      char2_pos = (0,0) #calculate this at some point loser

      #if dialoge["type"] == "text":
      #char1_surface = load_char_image(self.chars[0].get_sprite(dialogue["char_name"] + dialogue["emotion"].png))
      #char2_surface = load_char_image(self.chars[1].get_sprite(get_emotion()))

      #get whos talking from text
      # if none then blur out both (this usually mean inner dialogue)
      
      # for character who isnt talking -> lower saturation and maybe opacity

      #screen.blit(char1_surface, char1_pos)
      #screen.blit(char2_surface, char2_pos)

    #if there are no characters in the scene than we dont need to render anything at this stage.

    #next we need to render the text box
    if self.text_box == None:
      logger.push_log("Text box not set", True)
    else:
      screen.blit(self.text_box, self.text_box_pos)

    #check if the current dialogue is of type choice, or text

    #if text
    # render text box
  
    #if choice
    # render choices 


    # finally call flip to apply to screen
    pygame.display.flip()

    
    
  # def set_characters(new_chars []):
  #     pass
 
  def set_chars(self, new_chars):
     chars = new_chars

  def set_dialogue(self, new_dia: Scene.dialogue):
    if self.cur_dialogue != None:
      if self.cur_dialogue == new_dia:
        return
    
    self.cur_dialogue = new_dia
    logger.push_log("set dialoge " + str(self.cur_dialogue))

  # Sets the background file when the scene is changed 
  # NOTE: be sure to include the file extension in the parameter
  def set_bg(self, file_name: str):
      self.bg_img = pygame.image.load("Assets/bg_imgs/" + file_name)
      if self.bg_img == None:
          logger.push_log("bg_img " + file_name + " does not exist, check file name", True)
    
  pass

#will be called every frame before layering on the gui
  def reset_window(self):
      screen.fill("white")


  def get_window(self):
      return pygame.display.get_surface()

