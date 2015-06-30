Dag 11: Videre oppdatering av "winch" repository
################################################
:date: 2014-09-08 06:49
:author: Kristian Skurtveit
:email:	kristian.skurtveit@gmail.com 
:category: bachelorprosjekt
:tags: openstack, puppet, winch
:slug: dag-11-videre-oppdatering-av-winch-repository
:status: published

Siden "winch" ble laget for å støtte en eldre versjon av OpenStack ble
det nødvendig å oppdatere flere av puppet modulene til å nyeste versjon.
Uten dette feilet installasjonen momentant og det var ikke mulig å
provisjonere opp maskiner med puppet når modulene var utdaterte. Etter
at disse ble oppdatert gikk installasjonen overraskende nok gjennom. Vi
klarte å sette opp en controller node og en compute node.

Vi har tidligere holdt på med packstack som kjører alle OpenStack
komponentene på en og samme node. I et produksjonsmiljø vil vi heller
separere de ulike komponentene. Dette er av flere grunner; hver maskin
skal bare kunne gjøre det de er satt til, det vil lette trykket i
forhold til bare en og samme node, og det er mer oversiktlig og
skalerbart. Alle de forskjellige komponentene ligger under sine
respektive nett, her er en oversikt over hvordan det ser ut:

|RolesProfiles|

Etter at controller og compute noden kom opp kjørte vi de forskjellige
testene som fulgte med winch. Disse testene verifiserer funksjonalitet
og setter samtidig opp nettverk, rutere, og instanser.  Nå har vi en
kjørende instans og selve oppsettet ser ut til å fungere greit. Opplever
nå at instansen ikke kan nås fra controller noden, så dette er noe vi må
feilsøke videre på mandag.

.. |RolesProfiles| image:: http://openstack.b.uib.no/files/2014/09/RolesProfiles-1024x785.png
   :target: http://openstack.b.uib.no/files/2014/09/RolesProfiles.png
