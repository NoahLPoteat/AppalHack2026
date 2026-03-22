import pygame
import scene_handler

#make init
#setup boundry box
#get click detection
#setup on click 

class choice_button:

  norm_img = pygame.image.load("assets/gen/choiceBox.png")
  hvr_img = pygame.image.load("assets/gen/choiceBoxHov.png")

  width = 480
  height = 84
  margin = 4

  def __init__(self, pos, text, scene_hand, dest=None):
      self.pos = pos
      self.text = text
      self.dest = dest
      self.font = pygame.font.SysFont("Serif", 24)
      self.scene_hand = scene_hand
      self.rect = pygame.Rect(pos, (self.width, self.height))

  def draw(self, screen):
      # Change color on hover
      mouse_pos = pygame.mouse.get_pos()
      # print(mouse_pos)
      current_img = self.hvr_img if self.rect.collidepoint(mouse_pos) else self.norm_img
      
      screen.blit(current_img, self.pos)
      
      # Render da text
      text_surf = self.font.render(self.text, True, (255, 255, 255))
      text_rect = text_surf.get_rect(center=self.rect.center)
      screen.blit(text_surf, text_rect)

  def click(self, events):
    for event in events:
      # print (event)
      if event.type == pygame.MOUSEBUTTONDOWN:
         if event.button == 1:
            if self.rect.collidepoint(event.pos):
               self.on_click()

  def on_click(self):
    print(self.dest)
    if self.dest == None:
       self.scene_hand.set_scene("hell")
    else:
      self.scene_hand.set_scene(self.dest)