Dag 14: Oppdatering av Foreman og installasjon av compute noder
###############################################################
:date: 2014-09-17 15:33
:author: Kristian Skurtveit
:email:	kristian.skurtveit@gmail.com 
:category: bachelorprosjekt
:tags: 1.6, foreman, openstack, TFTP, winch
:slug: dag-14-oppdatering-av-foreman-og-installasjon-av-compute-noder
:status: published

Vi startet dagen med å feilsøke på hvorfor
`TFTP <http://en.wikipedia.org/wiki/Trivial_File_Transfer_Protocol>`__
serveren til Foreman ikke ville fungere. Flere problemer oppstod med
versjon 1.4.5 uten at vi fant noen gode forklaringer på hvorfor.
Maskinen som Foreman er installert på kjører en DHCP server og en TFTP
server. Disse tjenestene brukes når Foreman skal provisjonere opp
maskiner. Da blir maskinene PXE bootet og den henter ned det aktuelle
operativsystemet til maskinen og dette installeres automatisk.

Når en eldre pakke byr på problemer som ovenfor er løsningen som oftest
å oppdatere til nyeste versjon. Alle installeringsscriptene til Foreman
ble derfor modifisert slik at scriptet henter den nyeste programvaren
fra repositoriet. Etter at Foreman hadde komt opp til versjon 1.6
fungerte TFTP serveren og det var nå mulig å provisjonere opp maskiner.
Dette ble testet både på en fysisk maskin og på en virtuell maskin.

Når man skal provisjonere opp en maskin kan man velge fra en haug med
templater på hva innstillinger man ønsker osv. Foreman tilbyr mye
funskjonalitet og det er et stort verktøy å sette seg inn i. Heldigvis
er dette noe vi skal holde på med en god stund fremover, og det alltid
kjekt med bratte læringskurver.

Eksempelutdrag på et Foreman dashboard hentet fra google:

|foreman|

 

.. |foreman| image:: http://openstack.b.uib.no/files/2014/09/foreman.png
   :target: http://openstack.b.uib.no/files/2014/09/foreman.png
