# Određivanje pouzdanosti bežičnih komunikacijskih protokola
#
# Raspberry
Prije svega potrebno je povezati računalo s Raspberry Pijevima. Najlakši način je bežično preko WIFI mobilne pristupne točke. Potrebno je na SD karticu Raspberry računala unutar **boot** mape napraviti prazanu datoteku **SSH**. Zatim je potrebno napraviti datoteku **wpa_supplicant.conf**. Unutar datoteke potrebno je postaviti _Country Code_ (hr), naziv i lozinku WIFI mreže preko koje želimo s računala pristupiti Raspberryima.
Kako bi pristupili Raspberryima potrebno je biti sa računalom spojen na istu mrežu na koju smo konfigurirali Raspberryje.
Potrebno je otvoriti **terminal** unutar Linux operativnog sustava. u komandu liniju upišite: **ssh pi@rpi4.local** 
, gdje **rpi4** označava naziv Raspberryja u ovom slučaju. Ukoliko je sve dobro postavljeno i upisano, terminal će zahtjevati da upišete lozinku Raspberryja kako biste mogli pristupiti uređaju.

# Bluetooth
U terminalu na oba uređaja potrebno je ući u bluetooth postavke, to se postiže uspisujući u terminal naredbu: **bluetoothctl**. Na prvom uređaju zatim upisujemo: **scan on**, a na drugom: **discoverable on** i **pairable on**. Kada smo na prvom uređaju pronašli MAC adresu drugog, možemo zautaviti pretraživanje naredbom: **scan off**, zatim uparujemo uređaje naredbom: **pair  XX:XX:XX:XX:XX:XX**, gdje drugi dio naredbe predstavlja Mac adresu drugog uređaja. Iduće je potrebno unijeti narebu na oba uređaja: **trust  XX:XX:XX:XX:XX:XX** i MAC adresu suprotnog uređaja. Nakon toga možemo ih povezati: **connect  XX:XX:XX:XX:XX:XX**. 
#
Za pokretanje Blutooth programa potrebno se u terminalu pozicionirati unutar mapa sa programima.
1. Na prvom Raspberry Piu koji će primati poruke pokrećemo server.py:
  **python3 server.py**
  Ovako pokrenut program zapisivat će rezultate u terminal. Ukoliko želimo da nam se rezultati zapisiju u "datoteku", možemo pokrenuti program sa naredbama:
  **python3 server.py > datoteka**
  
2. Na drugom Raspberry Piu potrebno je pokrenuti client.py:
  **python3 client.py**
#
# Zigbee
Potrebno je uključiti XBee module u Raspberry.Za pokretanje Blutooth programa potrebno se u terminalu pozicionirati unutar mapa sa programima.
1. Na prvom Raspberry Pi pokrećemo receiver.py program koji će zapisivati mjerenja:
  **python receiver.py** ili opcionalno ukoliko želimo rezultate mjerenja primiti u "datoteku": **python receiver.py > datoteka**
2. Na drugom Raspberry Pi uređaju potrebno je pokrenuti transmitter.py: **python transmitter.py**
