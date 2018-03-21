## put Your thoughts into a file, clearing up your mind

# \tab == 3 spaces

import os
import time
from sys import exit
from re import sub

# ============================ FUNCTIONS: ==============================
def clearEntry(str = None):
   """displays an empty field for new text input"""
   os.system("cls" if os.name=="nt" else "clear") #TODO: detect if IDLE is used?
   print("\t\t\t\t*What's on Your mind, now?*")
   print("\n" * 8)
   if str == None: str = " >>  "
   return input(str)
   
def newEntry():
   while True:
      line = clearEntry()
      if line == "end":
         global goOn
         goOn = False
         return "\n"
      elif line == "showme":
         if os.name=="nt":
            os.system("notepad.exe "+path+sessName)
            #BUG: it's waiting till it closes, to proceed
         continue
      elif line == "showdir":
         if os.name=="nt":
            os.system("explorer.exe "+path)
         continue
      elif line == "help":
         clearEntry(" to commit, press [Enter]\n to exit the script, commit 'end'\n\n other possible commits are:\n  'showme'     opens current file in notepad\n  'showdir'    opens the folder containing the current session\n\n press [Enter] to continue now")
         #TODO: howto use it, purpose, etc.
         continue
      break
   
   line = stringFormatting(line)
   return line + "\n"

def stringFormatting(string=None):
   """formats the string for better indentation and listing"""
   if string == None:
      string=""
   string = sub("\t", " " * 3, string)
   if string and not string.startswith(" "): #BONUS: better noted "non empty"?
      string = "\n* " + string
      
   return string
   
def lineAppend(string=None):
   """
   writes input to a file and closes it, DOESN"T insert a newline after the entry!
   """
   if string == None:
      string=""
   myFile = open(path + sessName, "a+t")
   myFile.write(string)
   myFile.close()

# =============================== CODE: ================================
"""file of a session is named with the date & time of creation"""
initTimeString = time.strftime("%Y.%m.%d %H;%M,%S", time.localtime())
#TODO: act like it's six hours earlier, where dirname is concerned
   #if (time.localtime()==>)initTimeTuple[tm_hour] <= 5: 
   ## subtract 6h of TIME, and form an alternate tuple.. or use the-
   ## yeah, seems like working on tuples here is less convenient
   #TODO: get seconds & localtime to mingle nicely together #??
sessName = "ClearMind " + initTimeString[:10] + ".txt"   # date named session file
   
path = ".\\CM sessions\\" + initTimeString[:7] + "\\" # "YYYY.MM" named dir path
if not os.path.isdir(path):
   os.makedirs(path)
# -- init ends here --

# if fileExists(path + sessName):
   # lineAppend("\n\n==\n")
  
lineAppend(initTimeString + "\n")

goOn = True
while goOn:
   lineAppend(newEntry())

lineAppend(time.strftime("%Y.%m.%d %H;%M,%S", time.localtime()))

exit()

# ======================================================================
# if == "sublime":
   # myfile.sublimation()
   
# def sublimation():
   # """It's for quickly extracting useful thoughts from amongst the less important ones."""
   # while True:
      # #TODO: open a file --> and put next line into a variable
      # line = myFile.nextLine()   # jakiś licznik linijek tutaj?
      # if line.startswith("*"): a = input(line + "\n Press [Enter] to add it, otherwise press [Space],[Enter].")
      # if a == "":
         # line = line + linesThatFollow_withNoStar
         # #TODO: open file with simil name --> append to it
         # subFile.lineAppend(line)   # copy to "sublimed" file of the same name w/ suffix
      # else: continue
      # if EoF: 
         # print("some nice communicate")
         # break
         
#TODO: font size regulation & other formatting is VERY IMPORTATNT 
#  it lets you open the script wherever AND have your custom looks
#DONE: showme - opens the file in npp, or default system editor if None
#DONE: help - shows commands
#TODO: config file for custom command triggers, chosing the text editor, etc.
#TODO: shortcut for deleting whole current enrty w/o commiting
#TODO: taking args & modifying other list files in this manner
#  although maybe variation with '-' and no empty lines between + no end-time
#TODO: 
