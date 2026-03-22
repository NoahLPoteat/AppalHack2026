import scene
import logger
import choice_button

class scene_handler:
  current_scene = None
  current_lines: list[scene.dialogue]
  line_num: int = 0

  choice_buttons: list[choice_button.choice_button]
  
  
 
  def __init__(self, init_scene: str = "test"):
    self.set_scene(init_scene)

  #Just use the scene name, function automatically adds path and .json 
  def set_scene(self, scene_name: str):
    #begin trans


    if self.current_scene != None:
      if self.current_scene.name == scene_name:
        return
    self.current_scene = scene.loadJSON("scenes/" + scene_name + ".json")
    self.current_lines = self.current_scene.lines
    self.line_num = 0
    self.current_scene
    logger.push_log("Scene set to " + scene_name)

    #if window.transitioning == true
    # window.de_transition() #fades out the black box overlay


  #todo, if we reach end of lines, and there hasnt been a scene change we need to change scene to the default
  # IF no default, we need to change to hell.json
  def advance_line(self):
    print(self.current_lines[self.line_num])
    if self.current_lines[self.line_num] == "choice":
      self.choice_buttons = self.current_lines[self.line_num]

    if self.line_num >= len(self.current_lines) - 1:
      #if we are here, we have reached the end of the current scene, and no transistion has been made
      self.set_scene(self.current_scene.next_scene_default)
      pass
    else:
      self.line_num += 1
    
  def get_bg_file_name(self):
    return self.current_scene.bg

  def get_lines(self):
    return self.current_lines
  
  def get_current_scene_obj(self):
    return self.current_scene
  
  def get_current_scene_name(self):
    return self.current_scene.name
  
  def get_choices(self):
    return self.choice_buttons