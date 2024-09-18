import random
import time

import pyautogui as pag

while True:
    x = random.randint(100, 1000)
    y = random.randint(200, 1000)
    pag.moveTo(x, y, 0.5)
    time.sleep(2)
