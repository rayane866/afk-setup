# afk for minecraft by rayane866
import time
from pynput.keyboard import *
from pynput.mouse import Button, Controller
import logging 

mouse = Controller()
logging.basicConfig(filename='test.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')

print("This is an afk setup for minecraft created by rayane866\n \nF6: start/stop killing\nF7: start/stop fishing/placing blocks\nF8: start/stop breaking blocks\nF12: exit")
logging.info("running...")     

killing = False
fishing = False
breqking = False
running = True

st_killing = Key.f6
st_fishing = Key.f7
st_breqking = Key.f8
exit = Key.f12

def kill():                     #killing function
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(1)

def fish():                     #fishing function
    mouse.press(Button.right)


def breqk():                    #breaking function
    mouse.press(Button.left)

def on_press(key):              #detect the keys
    global killing, fishing, breqking, running

    if key == st_killing:       #for killing
        if killing:
            killing = False
            logging.info("stoped killing")
            print("[stoped killing]")
        else:
            breqking = False
            killing = True
            logging.info("killing...")
            print("[killing...]")

    elif key == st_fishing:     #for fishing
        if fishing:
            fishing = False
            mouse.release(Button.right)
            logging.info("stoped fishing/placing blocks")
            print("[stoped fishing/placing blocks]")
        else:
            fishing = True
            logging.info("fishing/placing blocks...")
            print("[fishing/placing blocks...]")

    elif key == st_breqking:    #for breaking
        if breqking:
            breqking = False
            mouse.release(Button.left)
            logging.info("stoped beaking blocks")
            print("[stoped beaking blocks]")
        else:
            killing = False
            breqking = True
            logging.info("breaking blocks...")
            print("[breaking blocks...]")

    elif key == exit:           #for exiting
        logging.info("exiting...\n")
        print("[exiting...]")
        running = False
        mouse.release(Button.right)
        mouse.release(Button.left)


def main():                     #the main functoin
    lis = Listener(on_press=on_press)
    lis.start()
    while running:
        if killing:             #for killing
            kill()
        elif fishing:           #for fishing
            fish()
        elif breqking:          #for breaking
            breqk()
    
main()      #starting program