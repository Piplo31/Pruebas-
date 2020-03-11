import curses
import time
snakeCola=0
snakeCabeza=0
snakex=0
snakey=0
dire=1
movx=False
movy=True
def addCola():
    snakeCola+=1

def direc(key):
    global movx
    global movy
    global dire
    dire=0
    movx=False
    movy=False
    if key=='w' or key=='a':
        dire=-1
    elif key=='s' or key=='d':
        dire= 1
    if key=='s' or key=='w':
        movy=True
    elif key=='a' or key=='d':
        movx=True
    return (dire,movx,movy)

def movSx(w):
    global snakex
    global movx
    global dire
    if movx==True :
        if snakex==1: 
            snakex=w-3
            return snakex
        elif snakex==w-2:
            snakex=2
            return snakex
        elif snakex<w-2:
            if dire==1:
               snakex+=1
               return snakex
            elif dire==-1:
               snakex-=1 
               return snakex
    return snakex
    
def movSy(h):
    global snakey
    global movy
    global dire
    if movy==True:                          
      if snakey==1:                   
          snakey=h-3               
          return  snakey             
      elif snakey==h-2:                
          snakey=2                   
          return snakey           
      elif snakey<h-2:           
          if dire==1:                       
              snakey+=1          
              return snakey     
          elif dire==-1:                    
              snakey-=1  
              return snakey
    return snakey


