import pyautogui as pg
import time


while True:
  pg.moveTo(1600, 600, 0, _pause=False) # cookie
  time.sleep(10)
  pg.moveTo(2900, 800, 0, _pause=False) # shipment
  pg.moveTo(2900, 320, 2, _pause=False) # cursor
  pg.moveTo(2900, 200, 0, _pause=False) #perks
  time.sleep(0.5)