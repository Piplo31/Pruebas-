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
    frutex,frutey=comida.randpos(stdscr)
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
        if snake.snakex==frutex and snake.snakey==frutey:
            existeFruta=False
            puntos+=10



        try:
         #stdscr.addstr(0,0,(str(snakex)+str(snakey)+str(dire)))
         stdscr.addstr(snake.snakey,snake.snakex,'■')
         #stdscr.addstr(0,0,str(movx)+str(movy))
        except: pass
        stdscr.addstr(0,0,str(puntos))
        comida.placeFood(stdscr,frutex,frutey)
        stdscr.refresh()
        tim=0.12
        if snake.movx: tim=0.08
        time.sleep(tim)
        if not existeFruta:
            frutex,frutey=comida.randpos(stdscr)
            existeFruta=True
    
    


