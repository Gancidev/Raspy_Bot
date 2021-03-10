# Raspy_Bot
Bot per comunicare con la propria raspberry

# Funzionamento
L'utente lancia un comando che poi il bot interpreta in modi diversi, i comandi 3 e 4 sono lanciati dalla libreria os e quindi riavvia/spegne la raspberry, mentre i comandi 1 e 2 sono generati dalla libreria subprocess il quale output viene elaborato per fornire i messaggi sull'ip locale o sullo stato della raspberry

# Comandi Disponibili
1. /ip : Comunica all'utente l'ip locale della raspberry
2. /status : Crea un piccolo report sull'utilizzo di memorie(RAM e MicroSD) e CPU
3. /reboot : Riavvia la raspberry.
4. /shutdown : Spegne la raspberry.

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
Per usufruire del bot è necessario inserire l'id della vostra chat facilmente visionabile lanciando lo script, mandando un messaggio al bot e leggendo dal terminale il campo chat valore id e aggiungere il Telegram Bot Token.
Per rendere il bot sempre attivo senza dover avere una sessione aperta sulla raspy si può trasformare lo script in un servizio linux mediante la seguente guida: https://github.com/torfsen/python-systemd-tutorial

E' necessario installare il pacchetto sysstat con il comando "apt-get install sysstat" per far funzionare correttamente il bot.
