import pyautogui
import time

pyautogui.click(1800,26, duration=1)
pyautogui.doubleClick(336,730, duration=1)

pyautogui.click(947, 595, duration=1)
pyautogui.click(983,541,duration=1)
pyautogui.write("Ana")
pyautogui.click(958,571,duration=1)
pyautogui.write("123456")
pyautogui.click(899,596,duration=1)

pyautogui.click(971,543,duration=1)
pyautogui.write("Ana")

pyautogui.click(967,568,duration=1)
pyautogui.write("123456")

pyautogui.click(874,598,duration=1)

with open(r'produtos.txt', 'r') as arquivos:
    for linha in arquivos:
        produto = linha.split(',')[0]
        quantidade = linha.split(',') [1]
        preco = linha.split(',')[2]

        pyautogui.click(674, 527, duration=1)
        pyautogui.write(produto)

        pyautogui.click(670, 556, duration=2)
        pyautogui.write(quantidade)

        pyautogui.click(674, 583, duration=2)
        pyautogui.write(preco)

        pyautogui.click(589,735,duration=2)