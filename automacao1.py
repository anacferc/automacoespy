import pyautogui # biblioteca python
# NATIVOS DO PYTHON nao precisa instalar
import time
import webbrowser # ABRIR O BROWSER (google, edge..)

pyautogui.moveTo(1804, 25, duration=1)
pyautogui.click()

webbrowser.open("https://youtube.com")
time.sleep(5) # coloca isso para o programa não se confundirMundo Canibal

pyautogui.moveTo(988,108, duration=1)
pyautogui.click()
pyautogui.write("Mundo Canibal")
pyautogui.press("enter")
pyautogui.scroll(-1200) # equivalente a um scroll
time.sleep(1)
pyautogui.scroll(-1200)
pyautogui.moveTo(670,869, duration=1)
time.sleep(3)
pyautogui.click()