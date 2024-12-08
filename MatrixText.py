import time
import random

alphabet = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!\"£$%&/()=\\|'ì?^è+é*òàùç°§[]@#{}<>,.-;:_ "
frase = "Nel bel mezzo del cammin di nostra vita mi ritrovai per una selva oscura che la retta via era smarrita."

def printstr(string):
  print(string)

def alphabetminusletter(letter):
  returnvalue = ""
  for k in alphabet:
    if (k!=letter):
      returnvalue += k
  return(returnvalue)

def writecooltext(sentence, timeperletter, repeattimes):
  writtensentence = ""
  for i in sentence:
      for j in range (0, repeattimes):
        if (j != repeattimes-1):
          printstr(writtensentence + alphabetminusletter(i)[random.randrange(0, len(alphabetminusletter(i)))])
        else:
          writtensentence = writtensentence + i
          printstr(writtensentence)
        time.sleep(timeperletter/repeattimes)

writecooltext(frase, 0.2, 20)
