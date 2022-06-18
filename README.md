# Određivanje pouzdanosti bežičnih komunikacijskih protokola


# Bluetooth
U terminalu na oba uređaja potrebno je ući u bluetooth postavke, to se postiže uspisujući u terminal naredbu: **bluetoothctl**.
Na prvom uređaju zatim upisujemo: **scan on**, a na drugom: **discoverable on** i **pairable on**. Kada smo na prvom uređaju pronašli MAC adresu drugog, možemo zautaviti pretraživanje naredbom:**scan off**, zatim uparujemo uređaje naredbom:**pair  XX:XX:XX:XX:XX:XX**, gdje drugi dio naredbe predstavlja Mac adresu drugog uređaja. Iduće je potrebno unijeti narebu na oba uređaja: **trust  XX:XX:XX:XX:XX:XX** i MAC adresu suprotnog uređaja. Nakon toga možemo ih povezati: **connect  XX:XX:XX:XX:XX:XX**. 
#
Za pokretanje Blutooth programa potrebno se u terminalu pozicionirati unutar mapa sa programima.
1. Na prvom Raspberry Piu koji će primati poruke pokrećemo server.py:
  **python3 server.py**
  Ovako pokrenut program zapisivat će rezultate u terminal. Ukoliko želimo da nam se rezultati zapisiju u "datoteku", možemo pokrenuti program sa naredbama:
  **python3 server.py > datoteka**
  
2. Na drugom Raspberry Piu potrebno je pokrenuti client.py:
  **python3 client.py**

# Zigbee
Potrebno je uključiti XBee module u Raspberry.Za pokretanje Blutooth programa potrebno se u terminalu pozicionirati unutar mapa sa programima.
1. Na prvom Raspberry Pi pokrećemo receiver.py program koji će zapisivati mjerenja:
  **python receiver.py** ili opcionalno ukoliko želimo rezultate mjerenja primiti u "datoteku": **python receiver.py > datoteka**
2. Na drugom Raspberry Pi uređaju potrebno je pokrenuti transmitter.py: **python transmitter.py**
