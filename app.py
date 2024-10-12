import pyautogui as pag 
from time import sleep

# Prints the resolution of the pc / laptop screen
print(pag.size())

# prints the current position of the mouse
print(pag.position())

# Moves the mouse over time (2) secs
#pag.moveTo(100, 100, 2)

# Moves the mouse over time (2) secs relatively
# sleep(1)
# pag.moveRel(100, 100, 2)

# Mouse clicks
# pag.click(500, 500, 2, 1, button="left")
# pag.tripleClick()
# pag.doubleClick()
# pag.leftClick()
# pag.rightClick()

# Mouse Scroll
#pag.scroll(1500) #scroll up
#pag.scroll(-1500) #scroll down


# sleep(2)
# pag.mouseDown(300, 400, button="left")
# pag.moveTo(500, 400)
# pag.mouseUp()
# sleep(1)
# pag.moveTo(700, 400)
# pag.mouseDown()
# sleep(1)
# pag.moveTo(900, 400)



# Spiral drawing using pyautogui
# sleep(2)
# distance = 300
# while distance > 0:
#     pag.dragRel(distance, 0, 1, button="left")
#     distance = distance - 20
#     pag.dragRel(0, distance, 1, button="left")
#     pag.dragRel(-distance, 0, 1, button="left")
#     distance = distance - 20
#     pag.dragRel(0, -distance, 1, button="left")
#     sleep(1)


# Keyboard functions
sleep(2)
pag.write("Hello world!")
pag.hotkey("ctrl", "c") 
pag.hotkey("ctrl", "v")
pag.press("enter")
pag.press("space")




