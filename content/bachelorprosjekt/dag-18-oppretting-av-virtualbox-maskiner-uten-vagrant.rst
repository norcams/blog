Dag 18: Oppretting av virtualbox maskiner uten vagrant
######################################################
:date: 2014-10-08 11:41
:author: Kristian Skurtveit
:email:	kristian.skurtveit@gmail.com 
:category: bachelorprosjekt
:tags: compute, controller, foreman, vagrant, winch
:slug: dag-18-oppretting-av-virtualbox-maskiner-uten-vagrant
:status: published

Onsdag 1. oktober var offisiel kickoff for UH-Sky prosjektet som jeg er
en del av. Fremover vil det være mye større aktivitet på github i form
av endringer enn tidligere. Til nå har arbeidet med "winch" vært preget
av mye feilsøking og manuell konfigurasjon. Det vi ønsker å oppnå er å
lage et helautomatisk oppsett for å deployere OpenStack i et testmiljø.

For å unngå en del problemer vi har opplevd tidligere har vi besluttet å
lage et script som oppretter virtualbox maskiner uten innblanding fra
vagrant. Vagrant låser blant annet eth0 interfacet og setter dette til
et NAT'et interface. Dette har ført til at maskiner ikke får TFTP bootet
når skal provisjonere disse med Foreman. I tillegg har vi fått en del
linux bro problematikk og det har krevd mye feilsøking for å få ting til
å fungere som de skal. For nå har jeg laget et script som vil opprette
de to komponentene
`compute <https://github.com/norcams/winch/blob/master/vagrant/create-vbox-compute.sh>`__\ og
`controller <https://github.com/norcams/winch/blob/master/vagrant/create-vbox-controller.sh>`__.
Senere vil vi nok også utvide scriptet til å gjelde for storage og
network også.
