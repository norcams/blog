Dag 2: OpenStack from scratch
#############################
:date: 2014-08-19 08:57
:author: Kristian Skurtveit
:email:	kristian.skurtveit@gmail.com 
:category: bachelorprosjekt
:tags: github, ofs
:slug: dag-2-openstack-from-scratch
:status: published

7. august gikk med til å utføre en OpenStack installasjon fra scratch.
Denne installasjonen gir et godt inntrykk av hva komponenter OpenStack
består av og hvordan disse skal fungere sammen i en komplett
installasjon.

Vi støtte på litt problemer etter installasjonen av OpenStack from
scratch. Noe av hovedfunksjonaliteten i systemet er å kunne lage og
bygge instanser av maskiner som skal kjøre i et driftsmiljø. Denne biten
feilet og vi har startet feilsøking av hva som kan ha gått galt. Dette
er noe vi kommer til å fortsette med i morgen.

OpenStack from scratch er et github prosjekt som er blitt laget i
forbindelse med prosjektet jeg er med i på UIB.  Hele prosjektet ligger
åpent på github -> https://github.com/norcams/ofs

Før jeg begynner å gå inn i detaljer om OpenStack, vil det være greit
for leserne å vite litt om bakgrunnen til programvaren og hva den brukes
til. Velger i denne sammenhengen å vise til
`Wikipedia <http://en.wikipedia.org/wiki/Openstack>`__\ artikkelen som
jeg syns har oppsummert dette ganske bra, samt at den forklarer bruken
til hver av komponentene.

|OpenStack|

.. |OpenStack| image:: http://openstack.b.uib.no/files/2014/08/OpenStack.png
