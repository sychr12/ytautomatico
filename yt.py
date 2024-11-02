import pyautogui
import time

pyautogui.PAUSE = 0.9

pyautogui.alert('Não perte em nada')
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.moveTo(417,229)
pyautogui.click()
time.sleep(1)


pyautogui.moveTo(320,64)
pyautogui.click()
time.sleep(1)

pyautogui.write('youtube')
pyautogui.press('Enter')
time.sleep(1)


pyautogui.moveTo(216,357)
pyautogui.click()
time.sleep(1)

pyautogui.moveTo(433,166)
pyautogui.click()
time.sleep(1)

pyautogui.write('Keyboard Cat! - THE ORIGINAL!')
pyautogui.press('Enter')
time.sleep(1)

pyautogui.moveTo(522,670)
pyautogui.click()
pyautogui.alert('Press F =(')
