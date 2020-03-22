import curses
import time
snakeCola=0
coordenadasCola=[]
snakeCabeza=0
snakex=0
snakey=0
dire=1
movx=False
movy=True
def addCola():
    global snakeCola
    global coordenadasCola
    snakeCola+=1
    coordenadasCola.append([0,0])


def dibujarCola(stdscr):
    global snakeCola
    global coordenadasCola

    for i in coordenadasCola:
            stdscr.addstr(i[1],i[0],'#')
            stdscr.refresh()
#■

def setCoordenadas(dire,axis):
    global snakex
    global snakey
        
    if dire==1:
        for i,j in  enumerate(coordenadasCola):
            if axis=="y":
                j[1]=snakey+i;
                j[0]=snakex;
            elif axis=="x":
                j[0]=snakex+i;
                j[1]=snakey;
    else:
         for i,j in enumerate(coordenadasCola):
            if axis=="y":
                j[1]=snakey-i;
                j[0]=snakex;
            elif axis=="x":
                j[0]=snakex-i;
                j[1]=snakey;
    
            


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
            setCoordenadas(dire,"x")  
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
          setCoordenadas(dire,"y")        
          if dire==1:  
             snakey+=1          
                  
          elif dire==-1:                    
              snakey-=1  
              


