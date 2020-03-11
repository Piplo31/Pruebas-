import random 

def randpos(stdscr):
  random.seed()
  h,w=stdscr.getmaxyx()
  x=random.randint(2,w-3)
  y=random.randint(2,h-3)
  return(x,y)


def placeFood(stdscr,x,y):
    
  stdscr.addstr(y,x,"●")
  stdscr.refresh()
        


