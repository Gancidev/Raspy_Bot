import os
import time
import telepot
from telepot.loop import MessageLoop
import subprocess

def handle(msg):
    print(msg)
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text' and chat_id == 151511468:
        if msg["text"]=="/ip":
            ip = subprocess.check_output("hostname -I", shell=True)
            bot.sendMessage(chat_id, "Indirizzo Locale:  "+str(ip))
        if msg["text"]=="/status":
            testo = subprocess.check_output("free -m", shell=True)
            test=testo.split("         ")
            messaggio="Stato RAM:\n Totale:"+test[2]+"MB\n In Uso: "+test[3]+"MB\n Disponibile: "+test[7].replace("\nSwap:","")+"MB"
            testo = subprocess.check_output("df -h", shell=True)
            test=testo.split("\n")
            tes=test[1].split(" ")
            messaggio=messaggio+"\n\nStato HDD:\n Totale: "+tes[7]+"B\n In Uso: "+tes[9]+"B\n Disponibile: "+tes[13]+"B"
            bot.sendMessage(chat_id, messaggio)
        if msg["text"]=="/reboot":
            bot.sendMessage(chat_id, "Sto riavviando la scheda.")
            os.system("reboot")
        if msg["text"]=="/shutdown":
            bot.sendMessage(chat_id, "Sto spegnendo la scheda, il bot non rispondera' fino alla sua accensione.")
            os.system("shutdown -h now")
TOKEN = '1288871500:AAFpLlV6Pox6sKzYv8czSFyfbJX4iIk93YE'

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
