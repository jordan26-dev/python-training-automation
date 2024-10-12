import pyautogui as pag
from time import sleep



# res =  pag.locateOnScreen("images/edit.png", confidence=0.8)
# print(res)

# x, y = pag.center(res)



x, y = pag.locateCenterOnScreen("images/edit.png", confidence=0.9)

pag.moveTo(x, y, 1)

pag.click()