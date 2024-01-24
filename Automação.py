import pyautogui
import time

pyautogui.PAUSE = 0.7

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(2)

pyautogui.click(x=872, y=525)

pyautogui.write("bsromeo@gmail.com")
pyautogui.press("tab")
pyautogui.write("minhasenha")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(2)

import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
  
    pyautogui.click(x=591, y=361)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))   
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")
    
    pyautogui.scroll(5000)