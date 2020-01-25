# P2D
Trasforma (quasi) qualsiasi cosa in un oggetto IoT / A new way to do IOT without pain!

Il progetto consiste in un set di dispositivi realizzati con le tecniche della fabbricazione digitale (tagliati al laser piuttosto che stampati 3d), basati su moduli wifi economici, che una volta applicati a oggetti come telecomandi, interruttori, etc sono in grado di trasformarli in dispositivi IoT controllabili remotamente attraverso un'unica interfaccia, che può essere un bot Telegram o una dashboard fisica.

Attraverso questa interfaccia sarà quindi possibile accendere luci, pilotare l'apertura di garage, o di altri dispositivi che siano dotati di un interruttore o di bottone. Non ci son cavi da saldare o modifiche da effettuate all'impianto elettrico: c'è solo da applicare il dispositivo P2D e configurarlo grazie alla sua interfaccia web.

Questo progetto permette di:
- agevolare persone con disabilità (problemi di mobilità in primis) fornendo un'interfaccia unificata (che sia touch o fisica) per controllare vari dispositivi distribuiti in tutta la casa
- creare nodi domotici economici, facilmente implementabili e completamente reversibili 
- condividere dispositivi "analogici" costosi (come telecomandi per garage) in modo che siano utilizzabili da tutta la famiglia con un semplice client Telegram 

Se c'è più di un dispositivo P2D, c'è bisogno di una RaspberryPi (un piccolo ed economico computer) che lavori da "gateway" tra Telegram ed essi.
Il sistema P2D è opensource e compatibile con i sistemi di home automation Souliss e OpenHab!

Certamente è possibile per chiunque creare (e condividere) i lproprio dispositivo P2D usando una stampante 3d, una lasercut o una cnc nel proprio laboratorio o in uno dei FabLab presenti in tutto il mondo!
La libreria di dispositivi P2D potrà continuare a crescere grazie agli utilizzatori che condivideranno le loro soluzioni.

// 
![enter image description here][1]
  
PhotoGallery:
http://bit.ly/P2D_pics
//

The project aims to create a set P2D devices based on cheap ESP\* wifi module, able to turn a physical device (like a remote, or a switch plate, ad so on) into one connected to the network.
So ie you can turn on the light, or open your garage using your Telegram client or by a physical dashboard.
You do not have to solder or to connect wires to your eletrical system!
Simply apply the P2D device and configure it through its web interface.

Thanks to this project you can:
- help people with disabilities, by giving them a single interface able to control devices in all their house
- create cheap domotic node, easy to implement and to remove
- "share" expensive devices so you (and i.e. your family) can control it by a Telegram client

If you have more than one device, you may need a raspberrypi (a cheap, small computer) to act as "gateway" between telegram and your home.
The P2D microsystem is opensource and is compatible with the Soluiss and OpenHab (https://www.openhab.org/) home automation 

Of course you can create (and then share!) your own P2D device by using a 3d printer / lasercutter / cnc at home or in one of the thousand of FabLab.
The library of the P2D device can continue growing thank to all the users who share their own device design.

[1]: https://lh3.googleusercontent.com/Twy0yCDc71v3AcBvC37XHgslUx01OOKUGx7Gx9bPAjsn0Cc4cEyD0cAH9VnTkGbFKlX5V1Ed-rWrJCrwVCvouirwrrYHMMccMCJP-SeGy4X18ismx4593OlzVvDEP1NpCRrCcnpI858=w897-h665-no
