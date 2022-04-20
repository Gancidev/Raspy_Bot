import os
import time
import telepot
from telepot.loop import MessageLoop
import subprocess

def handle(msg):
    print(msg)
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    #E' importante settare il chat_id nell'if perchè altrimenti chiunque potrebbe ricevere informazioni sulla nostra raspberry e causarne riavvii, spegnimenti e altro.
    if content_type == 'text' and chat_id == {YOUR CHAT_ID}:
        if msg["text"]=="/ip":
            ip = subprocess.check_output("hostname -I", shell=True)
            bot.sendMessage(chat_id, "Indirizzo Locale:  "+str(ip))
         if msg["text"]=="/stato":
            ram_totale = subprocess.check_output("free -m | grep Mem | awk '{print $2}'", shell=True)
            ram_usata = subprocess.check_output("free -m | grep Mem | awk '{print $3}'", shell=True)
            ram_disponibile = subprocess.check_output("free -m | grep Mem | awk '{print $7}'", shell=True)
            messaggio="Stato RAM:\n Totale: "+str(ram_totale,"utf-8")[:-1]+"MB\n In Uso: "+str(ram_usata,"utf-8")[:-1]+"MB\n Disponibile: "+str(ram_disponibile,"utf-8")[:-1]+"M>
            memoria_totale = subprocess.check_output("df -h | grep /dev/root | awk '{print $2}'", shell=True)
            memoria_in_uso = subprocess.check_output("df -h | grep /dev/root | awk '{print $3}'", shell=True)
            memoria_disponibile = subprocess.check_output("df -h | grep /dev/root | awk '{print $4}'", shell=True)
            messaggio=messaggio+"\n\nStato HDD:\n Totale: "+str(memoria_totale,"utf-8")[:-1]+"B\n In Uso: "+str(memoria_in_uso,"utf-8")[:-1]+"B\n Disponibile: "+str(memoria_dis>
            testo=subprocess.check_output("cat /sys/class/thermal/thermal_zone*/temp", shell=True)
            messaggio=messaggio+"\n\nStato CPU:\n Temperatura: "+str(testo,"utf-8")[:2]+"."+str(testo,"utf-8")[2:3]+"'C\n Utilizzo:"
            testo=subprocess.check_output("mpstat | grep all | awk '{print $NF}'",shell=True)
            tes=100-float(str(testo,"utf-8").replace(",","."))
            tes=round(tes,1)
            messaggio=messaggio+" "+str(tes)+"%"
            bot.sendMessage(chat_id, messaggio)
        if msg["text"]=="/reboot":
            bot.sendMessage(chat_id, "Sto riavviando la scheda.")
            os.system("reboot")
        if msg["text"]=="/shutdown":
            bot.sendMessage(chat_id, "Sto spegnendo la scheda, il bot non rispondera' fino alla sua accensione.")
            os.system("shutdown -h now")
TOKEN = '{YOUR TELEGRAM BOT TOKEN}'

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
