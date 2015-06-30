Dag 12: Feilsøking av "winch" installasjon
##########################################
:date: 2014-09-12 06:27
:author: Kristian Skurtveit
:email:	kristian.skurtveit@gmail.com 
:category: bachelorprosjekt
:tags: feilsøking, nettverk, openstack, winch
:slug: dag-12-feilsoking-av-winch-installasjon
:status: published

Fra tidligere har vi ofte hatt problemer med å få instanser til å snakke
med verden på utsiden. Dette har ofte krevd mer konfigurasjon og
feilsøking enn først antatt. Denne gangen var intet unntak. Det ble mye
repetering av OpenStack network in too much detail og sjekking av
brannmurregler for å verifisere at alt var i orden.

Etter en god del feilsøking viste det seg til slutt å være at feilen
oppstod på grunn av
`vagrant <http://en.wikipedia.org/wiki/Vagrant_%28software%29>`__. Vi
bruker vagrant til å lage virtuelle maskiner og denne hadde da stokket
om på IP adressene til de forskjellige interfacene maskinene skulle ha.
Derfor var det mye som ikke ble riktig og etterpå kunne maskinene komme
på nett. Senere i uken ble også "winch" prosjektet oppdatert. Endringer
kan sees `her <https://github.com/norcams/winch/tree/foreman>`__.
