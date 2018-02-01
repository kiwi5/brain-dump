## put Your thoughts into a file, clearing your mind

# \tab == 3 spaces

import os
import time
from sys import exit

# ======================================================================
def newEntry():
   '''displays an empty field for new text input'''
   #TODO: detect if IDLE is used
   os.system('cls' if os.name=='nt' else 'clear')
   
   #print("Newline: Ctrl-Enter   Commit: Enter   Escape: write 'End'")
   print("\t\t\t\t*What's on Your mind, now?*")
   print('\n' * 8)
   line = input(" >>  ")   # write in the middle of field (x lines below instructions)
   
   # if line == "end" or "exit":
   if line == "end":
      global goOn
      goOn = False
      return
   return line

def lineAppend(string=None):
   '''writes each entry to a LINE of a file and closes it'''
   myFile = open(path + sessName, 'a+t')
   
   if string == None:
      string=''
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

exit()

# ======================================================================
#TODO: font size regulation
