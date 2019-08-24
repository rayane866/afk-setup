# afk for minecraft by rayane866
import time
from pynput.keyboard import *
from pynput.mouse import Button, Controller

mouse = Controller()

print("This is an afk setup for minecraft created by rayane866\n \nF6: start/stop killing(left click/1sec)\nF7: start/stop fishing/placing blocks (right click)\nF8: start/stop breaking blocks (left click)\nF12: exit")
      
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
            print("[stoped killing]")
        else:
            breqking = False
            killing = True
            print("[killing]")

    elif key == st_fishing:     #for fishing
        if fishing:
            fishing = False
            mouse.release(Button.right)
            print("[stoped fishing/placing blocks]")
        else:
            fishing = True
            print("[fishing/placing blocks]")

    elif key == st_breqking:    #for breaking
        if breqking:
            breqking = False
            mouse.release(Button.left)
            print("[stoped beaking blocks]")
        else:
            killing = False
            breqking = True
            print("[breaking blocks]")

    elif key == exit:           #for exiting
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

if __name__ == '__main__':      #starting program
    main()