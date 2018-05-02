# put Your thoughts into a file, clearing your mind up

# \tab == 3 spaces

import os
import time
from sys import exit
from re import sub


# ============================ FUNCTIONS: ==============================
def clearEntry(string=None):
   """Displays an empty field for new text input."""
   os.system("cls" if os.name == "nt" else "clear")
   print("\t" * 4, end="")
   print("*What's on Your mind, now?*")
   print("\n" * 8)
   if string is None:
      string = " >>  "
   return input(string)


def newEntry():
   while True:
      line = clearEntry()
      # commands' section:
      if line == "end":
         global goOn
         goOn = False
         return   # "\n"
      elif line == "showme":
         if os.name == "nt":
            os.system(f"notepad.exe {dirPath}{sessName}")
         continue
      elif line == "showdir":
         if os.name == "nt":
            os.system(f"explorer.exe {dirPath}")
         continue
      elif line == "help":
         clearEntry("""
 to commit, press [Enter]
 to exit the script, commit 'end'

 other possible commits are:
  'showme'     opens current file in notepad
  'showdir'    opens the folder containing the current session

 press [Enter] to continue now """)
         continue
      break

   line = stringFormatting(line)
   return line + "\n"


def stringFormatting(string=None):
   """Formats the string for better indentation and listing."""
   if string is None:
      string=""
   string = sub("\t", " " * 3, string)
   if string and not string.startswith(" "):
      string = "\n* " + string
   return string


def lineAppend(string=None):
   """Writes input to a file and closes it, DOESN'T insert a newline after the entry!"""
   if string is None:
      string=""
   myFile = open(fullPath, "a+t")
   myFile.write(string)
   myFile.close()


# =============================== CODE: ================================
"""File of a session is named with the date & time of creation."""
initTimeString = time.strftime("%Y.%m.%d %H:%M'%S", time.localtime())
sessName = f"ClearMind {initTimeString[:10]}.txt"  # date-named session file
dirPath = f"./CM sessions/{initTimeString[:7]}/"   # "YYYY.MM"-named dir path
if os.name is "nt":
   dirPath = sub("/", r"\\", dirPath)
if not os.path.isdir(dirPath):
   os.makedirs(dirPath)

fullPath = dirPath + sessName
if os.path.exists(fullPath):
   lineAppend("\n\n==\n")
# -- init ends here --

lineAppend(f"{initTimeString}\n")

goOn = True
while goOn:
   lineAppend(newEntry())

lineAppend("\n")
lineAppend(time.strftime("%Y.%m.%d %H;%M,%S", time.localtime()))

exit()