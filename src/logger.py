from datetime import datetime
from pathlib import Path
import io

#Called before the main loop
def create_log_file():
  global log_file 
  cur_time = datetime.now()
  time_f = str(cur_time)[:-7].replace(':', '-')
  
  path = Path("logs") / (time_f + ".txt")

  log_file = open(path, "w")
  push_log("Log File made")

def push_log(message: str, is_error: bool = False):
  post_fix: str = ""
  cur_time = datetime.now()
  time_f = str(cur_time)[:-7].replace(':', '-')
  if is_error:
    post_fix = "ERROR"

  log_file.write(time_f  + "| " + message + " | " + post_fix + "\n")

# Called when loop ends
def close_logger():
  log_file.close()

# create_log_file()
# push_log("testing logger")
# push_log("Logger Working")
# close_logger()