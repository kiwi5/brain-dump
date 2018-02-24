## put Your thoughts into a file, clearing your mind

# \tab == 3 spaces

import os
import time
from sys import exit
from re import sub

# ======================================================================
def newEntry():
   '''displays an empty field for new text input'''
   #TODO: detect if IDLE is used?
   os.system('cls' if os.name=='nt' else 'clear')
   
   #print("Newline: Ctrl-Enter   Commit: Enter   Escape: write 'End'")
   print("\t\t\t\t*What's on Your mind, now?*")
   print('\n' * 8)
   line = input(" >>  ")   # write in the middle of field (x lines below instructions)
   
   # if line == "end" or "exit":
   if line == "end":
      global goOn
      goOn = False
      return #None
   return line

def lineAppend(string=None):
   '''writes each entry to a LINE of a file and closes it'''
   myFile = open(path + sessName, 'a+t')
   
   if string == None: #or goOn == False:
      string=''
   string = sub('\t', ' ' * 3, string)
   if not string.startswith(' ') and string:
      #TODO: better noted that "non empty"
      string = '* ' + string
      
   myFile.write(string + '\n')
   
   myFile.close()

# =============================== CODE: ================================
'''
file of a session is named with the date & time of creation
'''
initTimeTuple = time.localtime()
initTimeString = time.strftime('%Y.%m.%d %H;%M,%S', initTimeTuple)
#if initTimeTuple[tm_hour] <= 5: 
   #TODO: act like it's six hours earlier, where dirname is concerned
   ## subtract 6h of TIME, and form an alternate tuple.. or use the-
   ## yeah, seems like working on tuples here is less convenient
   #TODO: get seconds & localtime to mingle nicely together
path = '.\\CM sessions\\' + initTimeString[:10] + '\\'

if not os.path.isdir(path):
   os.makedirs(path)
   
sessName = 'ClearMind ' + initTimeString + '.txt'

myFile = open(path + sessName, 'a+t')
myFile.write(initTimeString + '\n\n')
myFile.close()

goOn = True
while goOn:
   lineAppend(newEntry())

endTimeTuple = time.localtime()

myFile = open(path + sessName, 'a+t')
myFile.write(time.strftime('%Y.%m.%d %H;%M,%S', endTimeTuple))
myFile.close()
#TODO: open the just closed file in a Notepad++, for example

exit()

# ======================================================================
#TODO: font size regulation & other formatting is VERY IMPORTATNT 
#  it lets you open the script wherever AND have your custom looks
#TODO: if not startswith(' ') (or startswith(*)?): print that line
#  if Enter: append its copy to "sublimed" file of the same name w/ suffix
#  elif w/e: show next such line
#  it's for quickly extracting useful thoughts from amongst the less important ones
#TODO: 
#TODO: 
#TODO: 
#TODO: 
#TODO: 
