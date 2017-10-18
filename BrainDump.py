# createFile()
# lineAppend()
# newEntry()
# clearField()
# interPend()
# goodOnes()

# ======================================================================
def createFile(date.time()):
# opening session generates file
   # file of a session is named according to the date & time created

def firstLine("time.begin - time.end | session.duration:"):
# first line of a file contains date of beginning
   # and at the end is modified: maybe put there some unique str, and replace it?
   lineAppend(date() +" "+ time() +"endTime-placeholder")
   #TODO: +endDate if session across the midnight
   #BONUS: as well as summation of how long the session has taken, and nr of entries

def newEntry():
# displays an empty field for new text input
   #TODO: put this in infinite loop
   eraseField()
   # display instructions/shortcuts at the top of field
   print("Newline: Shift-Enter   Commit: Enter   Escape: write 'End'")
   print()
   print()
   print()
   print("What's on Your mind, now?")
   # write in the middle of field (or x lines below instructions)
   line = input(" >>  ")
   lineAppend(line)

def lineAppend():
# writes each entry to a LINE of a file
   # BONUS: newlines are replaced w/ "|"s  &&  S-Enter == newline

# ======================================================================
def interPend():
#BONUS: new entry w/o submitting current one
   # it is shown again afterwards
   # simple shortcut to do it QUICKLY
   # empty line is left where this'd be, and entry is prepended with nr of that line

def goodOnes():
#BONUS: after closing session: option to view contents line-by-line, and mark them as 'good ideas'
   # WORKING: open copied file in N++ > rm lines you don't like using C-S-l
   # reacts to (displayed) keys
   # creates new file out of chosen entries - old name appended w/ "chosen" etc.

#BONUS: font size regulation

# =============================== CODE: ================================
createFile()
firstLine()
while True:
   newEntry()
   if lastLine == "End":
      return