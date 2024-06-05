import pyautogui
from tkinter import *
from time import sleep


def credito():

    pyautogui.click(182,218)
    sleep(0.5)
    pyautogui.click(769,423)
    pyautogui.press("enter",presses=3)
    pyautogui.typewrite("1")
    pyautogui.press("enter",presses=2)
    pyautogui.press("space",presses=1)

    resposta=pyautogui.confirm(text="Continuar?", title="Confirmacao", buttons=["sim","nao"])
    if resposta == "sim":
        pyautogui.click(569,929)
        pyautogui.press("enter",presses=3,interval=0.5)
        pyautogui.press("enter",presses=4,interval=0.5)
        pyautogui.press("enter",presses=5,interval=0.5)
        sleep(0.5)
        pyautogui.press("esc")
        pyautogui.click(591,696,button="right",duration=0.5)
        pyautogui.click(668,709,duration=0.5)
        sleep(1)
        pyautogui.press("esc")
        pyautogui.click(590,770,duration=0.5)
        pyautogui.tripleClick(988,564,duration=0.5)
        sleep(1)
        
    else:
        print("Voce escolheu nao continuar")


def debito():
    
    pyautogui.click(182,218)
    sleep(0.5)
    pyautogui.click(735,442)
    pyautogui.press("enter",presses=3)
    pyautogui.typewrite("1")
    pyautogui.press("enter",presses=2)
    pyautogui.press("space",presses=1)

    resposta=pyautogui.confirm(text="Continuar?", title="Confirmacao", buttons=["sim","nao"])
    if resposta == "sim":
        pyautogui.click(569,929)
        pyautogui.press("enter",presses=3,interval=0.5)
        pyautogui.press("enter",presses=4,interval=0.5)
        pyautogui.press("enter",presses=5,interval=0.5)
        sleep(0.5)
        pyautogui.press("esc")
        pyautogui.click(591,696,button="right")
        pyautogui.click(668,709,duration=0.3)
        sleep(1)
        pyautogui.press("esc")
        pyautogui.click(590,770,duration=0.3)
        pyautogui.tripleClick(988,564,duration=0.3)
        sleep(1)
        
    else:
        print("Voce escolheu nao continuar")

    
def pix():

    pyautogui.click(182,218)
    sleep(0.5)
    pyautogui.click(808,491)
    pyautogui.press("enter",presses=2)
    pyautogui.typewrite("1")
    pyautogui.press("enter",presses=2)
    pyautogui.press("space",presses=1)

    resposta=pyautogui.confirm(text="Continuar?", title="Confirmacao", buttons=["sim","nao"])
    if resposta == "sim":
        pyautogui.click(569,929)
        pyautogui.press("enter",presses=3,interval=0.5)
        pyautogui.press("enter",presses=4,interval=0.5)
        pyautogui.press("enter",presses=5,interval=0.5)
        sleep(0.5)
        pyautogui.press("esc")
        pyautogui.click(591,696,button="right")
        pyautogui.click(668,709,duration=0.3)
        sleep(1)
        pyautogui.click(590,770,duration=0.3)
        pyautogui.tripleClick(988,564,duration=0.3)
        sleep(1)
        
    else:
        print("Voce escolheu nao continuar")


tela = Tk()
tela.geometry("+1200+200")
tela.title("Vendas")

botao_cred = Button(tela,text="Credito", command=credito,width=7, height=3)
botao_cred.grid(row=0, column=0)
botao_deb = Button(tela, text="Debito", command=debito, width=7, height=3)
botao_deb.grid(row=0, column=1)
botao_pix = Button(tela, text="Pix", command=pix, width=7, height=3)
botao_pix.grid(row=0, column=2)



tela.mainloop()
