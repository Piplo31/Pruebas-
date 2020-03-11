import curses
import time
import init
menu=["Jugar","options","exit"]

def printmenu(stdscr,num):
    stdscr.clear()
    h,w= stdscr.getmaxyx()
    for idx,txt in enumerate(menu):
        x=w//2 -len(txt)//2
        y=h//2-len(menu)+idx
        curses.init_pair(1,curses.COLOR_BLACK,curses.COLOR_WHITE)
        if idx==num:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y,x,txt)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y,x,txt)
    

    stdscr.refresh()


def main(stdscr):
    stdscr.clear()
    row=0
    printmenu(stdscr,row)

    while(1):
        key=stdscr.getch()
        if key==curses.KEY_UP and row>0:
            row-=1
        elif key==curses.KEY_DOWN and row<len(menu)-1:
            row+=1
        elif key==curses.KEY_ENTER or key in [10,13]:
            if menu[row]=="Jugar":
                stdscr.clear()
                h,w=stdscr.getmaxyx()
                x=w//2 
                y=h//2
                init.main(stdscr)
                #stdscr.addstr(y,x,"hola")
                stdscr.refresh()
                time.sleep(3)

        printmenu(stdscr,row)

curses.wrapper(main)



