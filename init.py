import snake
import curses
import time
import comida

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    #stdscr.clear()
    curses.init_pair(1,curses.COLOR_BLACK,curses.COLOR_WHITE)
    h,w=stdscr.getmaxyx()   
    snake.snakex=w//2
    snake.snakey=h//2 
    snake.movx=False
    snake.movy=True
    existeFruta=False
    comida.randpos(stdscr)
    snake.dire=1
    puntos=0
    cola=[]
    stdscr.refresh()
    key='s'
    while(True):
        stdscr.clear()
        try:
           key=stdscr.getkey() 
           if(key=="w" or key=="a"or key=="s"or key=="d"):
             snake.direc(key)
         
        except: pass

        snake.movSy(h)
        snake.movSx(w)
        if snake.snakex==comida.frutex and snake.snakey==comida.frutey:
            existeFruta=False
            puntos+=10
            snake.addCola()

        try:
         stdscr.addstr(snake.snakey,snake.snakex,'#')
         if(snake.snakeCola != 0):
             snake.dibujarCola(stdscr)

       
        except: pass

        stdscr.addstr(0,0,str(puntos)+" "+str(snake.snakeCola))
        comida.placeFood(stdscr,comida.frutex,comida.frutey)
        stdscr.refresh()
        tim=0.12
        if snake.movx: tim=0.08
        time.sleep(tim)
        if not existeFruta:
            comida.randpos(stdscr)
            existeFruta=True
    
    


