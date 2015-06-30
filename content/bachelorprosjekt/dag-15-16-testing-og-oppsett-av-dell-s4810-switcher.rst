Dag 15 & 16: Testing og oppsett av Dell s4810 switcher og feilsøking av puppet moduler
######################################################################################
:date: 2014-09-29 06:10
:author: Kristian Skurtveit
:email:	kristian.skurtveit@gmail.com 
:category: bachelorprosjekt
:tags: cumulus linux, dell, gilgamesh, omo, openstack, switcher, winch
:slug: dag-15-16-testing-og-oppsett-av-dell-s4810-switcher
:status: published

Mandagen ble brukt til å konfigurere opp to nye `Dell s4810
switcher <http://www.dell.com/learn/us/en/04/shared-content~data-sheets~en/documents~dell_force10_s4810_spec_sheet.pdf>`__
som skal brukes til testformål i prosjektet. I motsetning til andre
switcher som typisk kjører sitt eget operativsystem kjører disse
switchene på Linux. Cumulus Linux er en variant av Debian og det er
slike switcher som skal benyttes når den endelige skyplattformen
installeres. Oppsettet vi laget og monterte i rack kan visualiseres på
denne måten:

|iaas ruting-redundans test - Network general-1|

I tillegg har vi også jobbet videre med Foreman. Det er en del problemer
som gjenstår før vi kan fullprovisjonere maskiner ved hjelp av puppet
moduler. Etter at Foreman har provisjonert en maskin sliter vi med å få
puppet modulene til å virke på maskinen. Fra tidligere fungerte modulene
etter vi hadde oppdatert dem i forbindelse med "winch" prosjektet.
Eneste endringen nå er at vi bruker Foreman. Videre feilsøking på
mandag...

.. |iaas ruting-redundans test - Network general-1| image:: http://openstack.b.uib.no/files/2014/09/iaas-ruting-redundans-test-Network-general-1-1024x633.png
   :target: http://openstack.b.uib.no/files/2014/09/iaas-ruting-redundans-test-Network-general-1.png
