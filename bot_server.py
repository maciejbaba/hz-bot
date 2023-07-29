import pyautogui as pg
import time
while True:
  pg.moveTo(200, 400, 0, _pause=False) # cookie
  time.sleep(10)
  pg.moveTo(1220, 630, 0, _pause=False) # bottom of the list
  pg.moveTo(1220, 280, 2, _pause=False) # cursor
  pg.moveTo(1220, 220, 0, _pause=False) #perks
  time.sleep(0.5)
