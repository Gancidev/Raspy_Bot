# Raspy_Bot
Bot per comunicare con la propria raspberry

# Comandi Disponibili

1. /ip : permette all'utente di settare una città di default.
2. /status : mostra le previsioni meteo per la città di default.
3. /reboot : mostra le previsioni meteo per la città specificata.
4. /shutdown : mostra un messaggio che riassume il funzionamento del bot all'utente.

# Implementazione

Per la realizzazione sono state implementate le seguenti librerie: telepot, subprocess, os.
Il linguaggio utilizzato è il Python.

# Telepot

Una Libreria che permette di gestire attraverso se stessa un bot di telegram fornendo delle funzioni che si appoggiano alle API di telegram stesso.
E' stata utilizzata per la gestione dei messaggi che un utente e il bot scambiano.

# Subprocess

Una libreria che permette di lanciare processi di sistema salvandone l'output in una variabile dello script, utilizzata per estrarre informazioni sul sistema e mostrarle all'utente.

# Os

La libreria viene utilizzata per lanciare comandi di sistema, è stata utilizzata per eseguire i comandi 3 e 4 lanciati tramite il bot.

# Installazione e Utilizzo

Per poter eseguire lo script sarà necessario installare le opportune librerie indicate sopra.
Per usufruire del bot invece è necessario inserire l'id della vostra chat facilmente visionabile lanciando lo script, mandando un messaggio al bot e leggendo dal terminale il campo chat valore id.

Per rendere il bot sempre attivo senza dover avere una sessione aperta sulla raspy si può trasformare lo script in un servizio linux mediante la seguente guida: https://github.com/torfsen/python-systemd-tutorial
