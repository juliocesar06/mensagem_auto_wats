#1 importar bibliotecas
import pywhatkit
import keyboard
import time
from datetime import date, datetime
#2 definir contatos

# lista de contatos
contatos = ["""colocar os contatos aqui dentro separando por virgulas ex +5531987654321,"""]

#3 definir intervalo
i = 0
while len(contatos) >= 1:
    pywhatkit.sendwhatmsg(contatos[i],'ultimo teste...',datetime.now().hour,datetime.now().minute+1)
    del contatos[i]
    time.sleep(30)
    keyboard.press_and_release('ctrl + w')
    i += 1
