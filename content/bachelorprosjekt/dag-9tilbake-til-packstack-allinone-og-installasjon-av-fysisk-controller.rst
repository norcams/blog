Dag 9:Tilbake til packstack --allinone og installasjon av fysisk controller
###########################################################################
:date: 2014-09-03 06:03
:author: Kristian Skurtveit
:email:	kristian.skurtveit@gmail.com 
:category: bachelorprosjekt
:tags: allinone, feilsøking, nettverk, openstack, packstack
:slug: dag-9tilbake-til-packstack-allinone-og-installasjon-av-fysisk-controller
:status: published

Etter at minnetildelingen hadde blitt økt flere ganger på vår virtuelle
controller node bestemte vi oss for å installere denne på en fysisk
maskin. I tillegg hadde vi også hatt problemer med neutron-server, så i
denne omgang gikk vi tilbake på å kjøre packstack --allinone. Dette
ville forhåpentligvis gjøre slik at vi unngikk flere problemer,
hvertfall nå som vi er i en testfase.

Vi installerte på samme måte som tidligere. Fra før av har man en helt
ny installasjon av CentOS, og dermed følger man de `tre
stegene <https://openstack.redhat.com/Quickstart>`__\ som jeg har
skrevet om tidligere
`her <http://openstack.b.uib.no/2014/08/21/dag-4-installasjon-av-openstack-packstack/>`__. Noen
av de tingene vi har slitt med fungerte med en gang. Både neutron-server
og det å lage instanser fungerte uten problemer.

Det som gjenstår nå er å kunne få instansene til å snakke med verden på
utsiden. Dette gjør vi ved å utføre noen av de siste stegene i
`OpenStack network in to much
detail <https://openstack.redhat.com/Networking_in_too_much_detail#NAT_to_host_address>`__.
Det blir satt en offentlig IP adresse til OpenStack på br-ex interfacet.
Samtidig som vi legger til brannmurregler slik at trafikk på innsiden av
skyen blir maskert og videresendt gjennom noden og videre ut på  nettet.
Vi fikk litt problemer etter at reglene var lagt inn i brannmuren.
Instansene klarer ikke å pinge ut i verden. Det eneste instansen klarer
å pinge er controller noden og vice versa.

|Neutron_architecture|

 

.. |Neutron_architecture| image:: http://openstack.b.uib.no/files/2014/08/Neutron_architecture-300x166.png
   :target: http://openstack.b.uib.no/files/2014/08/Neutron_architecture.png
