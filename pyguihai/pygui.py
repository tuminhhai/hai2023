import time
import pyautogui

coors = pyautogui.locateOnScreen('h.png', grayscale=True, confidence=0.7)
coors_center = pyautogui.center(coors)
pyautogui.click(coors_center.x, coors_center.y)
time.sleep(5)

coors = pyautogui.locateOnScreen('g.png', grayscale=True, confidence=0.9)
coors_center = pyautogui.center(coors)
pyautogui.click(coors_center.x + 50, coors_center.y)
pyautogui.typewrite('facebook.com')
pyautogui.press('enter')
time.sleep(7)

coors = pyautogui.locateOnScreen('l.png', grayscale=True, confidence=0.7)
coors_center = pyautogui.center(coors)
pyautogui.click(coors_center.x, coors_center.y)
time.sleep(2)
pyautogui.typewrite('a loi')

time.sleep(2)
coors = pyautogui.locateOnScreen('anh dang.png', grayscale= True, confidence =0.9)
coors_center = pyautogui.center(coors)
pyautogui.click((coors_center.x)+50,(coors_center.y))
pyautogui.press('enter')
