import pygame
import logger
import scene as Scene
import choice_button as ChoiceButton
import textwrap

class Window:
  bg_img: pygame.Surface = None

  #= load(textbox.png) or something like that
  text_box: pygame.Surface = pygame.image.load("Assets/gen/text_box.png") 
  text_box_pos = (40,216) #based on text box being 560x144
  
  cur_dialogue: Scene.dialogue = None
  cur_scene_name: str = ""
  chars = [] 

  #choice button variables
  choice_buttons: list[ChoiceButton.choice_button]
  button_height: int = 84
  
  #we will have a static first, then each after will be done via math
  button_pos_x = 80 
  button_pos_y = 36 #add height - margin for each iteration
  button_margin = 8
  
  #FONT
  font:pygame.font = None

  dark_grey = (99,99,99) #will be button color when hovered
  light_grey = (66,66,66) #normal button color


  def __init__(self, win_width: int, win_height: int):
        global screen 
        screen = pygame.display.set_mode((win_width, win_height))
        self.font = pygame.font.SysFont("Serif", 30)

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
    # print(self.chars)
    if len(self.chars) == 1:
      char_pos = (192, 16) #centered for one character
      # print(self.chars[0])
      if self.cur_dialogue["type"] == "text":
          
        char_surface = pygame.image.load("assets/char_imgs/" + self.chars[0] + 
                                         self.cur_dialogue["emotion"] + ".png")
        screen.blit(char_surface, char_pos)

    elif len(self.chars) == 2:
      char1_pos = (12,16) #calculate this at some point loser
      char2_pos = (326,16) #calculate this at some point loser

      char1_surface: pygame.surface

      char2_surface: pygame.surface
      
      n = 0
      for char in self.chars:
        if char == self.cur_dialogue["speaker"]:
            if n == 0: #char 1 is talking
              char1_surface = pygame.image.load("assets/char_imgs/" +
                                        self.chars[0] + self.cur_dialogue["emotion"] + ".png")

              char2_surface = pygame.image.load("assets/char_imgs/" +
                                        self.chars[1] + "basic" + ".png")
              

              char2_surface.set_alpha(100)


              screen.blit(char1_surface, char1_pos)
              screen.blit(char2_surface, char2_pos)

            else:
              char1_surface = pygame.image.load("assets/char_imgs/" +
                                        self.chars[0] + "basic" + ".png")

              char2_surface = pygame.image.load("assets/char_imgs/" +
                                        self.chars[1] + self.cur_dialogue["emotion"] + ".png")
              
              char1_surface.set_alpha(100)

              screen.blit(char1_surface, char1_pos)
              screen.blit(char2_surface, char2_pos)

        n += 1
      
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
    if self.cur_dialogue["type"] == "text":
      text_rect_pos = (60, 253)
      box_wid = 515
      box_hei = 115
      rect = pygame.Rect(text_rect_pos, (box_wid, box_hei))
      
      words = self.cur_dialogue["text"].split(' ')
      lines = []
      current_line = ""

      for word in words:
          test_line = current_line + word + " "
          if self.font.size(test_line)[0] < rect.width:
              current_line = test_line
          else:
              lines.append(current_line)
              current_line = word + " "
      lines.append(current_line)

      y_offset = 0
      line_height = self.font.get_linesize()
      for line in lines:
          if y_offset + line_height > rect.height:
              break
          text_surface = self.font.render(line.strip(), True, (255, 255, 255))
          screen.blit(text_surface, (rect.x, rect.y + y_offset))
          y_offset += line_height
    

    #if choice
    # render choices 
    
    button_mod: int = 0
    if self.cur_dialogue["type"] == "choice":
      #render box to have a greyed out background
      overlay = pygame.Surface((640, 360), pygame.SRCALPHA)
      overlay.fill((128, 128, 128, 128)) 

      screen.blit(overlay, (0, 0))  

      for choice in self.cur_dialogue["choices"]:
        ch: Scene.choice = choice
        button = ChoiceButton.choice_button((self.button_pos_x,
                                 (self.button_pos_y + (self.button_height * button_mod) + self.button_margin * button_mod - 1 )),
                               ch["text"], self, ch["next_scene"]
                               )
        button.draw(screen)

        button_mod += 1

         

      #use pygame to create buttons, side note, figure out how to do that.
      #  print("doing a choice rn")
      pass


    # finally call flip to apply to screen
    pygame.display.flip()

    
    
  # def set_characters(new_chars []):
  #     pass
 
  def set_chars(self, new_chars):
    
     self.chars = new_chars

  def set_dialogue(self, new_dia: Scene.dialogue):
    if self.cur_dialogue != None:
      if self.cur_dialogue == new_dia:
        return
    
    self.cur_dialogue = new_dia
    logger.push_log("set dialogue " + str(self.cur_dialogue))

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

