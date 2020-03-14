import random 

frutex=0
frutey=0
def randpos(stdscr):
  global frutex
  global frutey
  random.seed()
  h,w=stdscr.getmaxyx()
  frutex=random.randint(2,w-3)
  frutey=random.randint(2,h-3)
  


def placeFood(stdscr,x,y):
    
  stdscr.addstr(y,x,"●")
  stdscr.refresh()
        


