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
    global snakeCola
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
        
        elif snakex==w-2:
            snakex=2
        
        elif snakex<w-2:
            if dire==1:
               snakex+=1
            
            elif dire==-1:
               snakex-=1 
            

    
def movSy(h):
    global snakey
    global movy
    global dire
    if movy==True:                          
      if snakey==1:                   
          snakey=h-3               
                      
      elif snakey==h-2:                
          snakey=2                   
                    
      elif snakey<h-2:           
          if dire==1:                       
              snakey+=1          
                  
          elif dire==-1:                    
              snakey-=1  
              
def dibujarCola(stdscr):
    global snakeCola

    for i in range(snakeCola):
         stdscr.addstr(0,0,'■')
         stdscr.refresh()
         time.sleep(10)

