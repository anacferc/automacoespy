import pyautogui
import time
import webbrowser
import pyperclip

pyautogui.moveTo(1808, 25, duration=1)
pyautogui.click()

webbrowser.open("https://www.linkedin.com/feed/")
time.sleep(5)
pyautogui.moveTo(857, 182, duration=1)
pyautogui.click()
time.sleep(1)
pyautogui.moveTo(619, 243, duration=1)
pyautogui.click()
<<<<<<< HEAD
texto = "🎆 Olá pessoal, estou aprendendo a realizar automações simples e essa mensagem foi feita por uma automação que foi ensinada pelo meu professor @Gessiel Silva, estamos iniciando esse conteúdo e é louco o quando a tecnologia pode realizar. Isso é apenas uma das várias coisas que a automação em Python pode realizar. Link do meu projeto no Git Hub: https://github.com/anacferc/automacoespy/blob/main/linkedin.py "
=======
texto = "🎆 Olá pessoal, estou aprendendo a realizar automações simples e essa mensagem foi feita por uma automação que foi ensinada pelo meu professor @Gessiel Silva, estamos iniciando esse conteúdo e é louco o quando a tecnologia pode realizar. Isso é apenas uma das várias coisas que a automação em Python pode realizar. Link do meu projeto no Git Hub: https://github.com/anacferc/automacoes/blob/main/linkedin.py "
>>>>>>> 00c8d3d9ad37c0430030ad8e425dac478863f174
pyperclip.copy(texto)
time.sleep(1)
pyautogui.hotkey("ctrl", "v")
pyautogui.moveTo(1258, 688, duration=1)
<<<<<<< HEAD
pyautogui.click()
=======
>>>>>>> 00c8d3d9ad37c0430030ad8e425dac478863f174
