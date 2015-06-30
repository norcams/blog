Dag 7: OpenStack networking in too much detail & feilsøking av neutron-server
#############################################################################
:date: 2014-08-27 06:22
:author: Kristian Skurtveit
:email:	kristian.skurtveit@gmail.com 
:category: bachelorprosjekt
:tags: compute, neutron, openstack
:slug: dag-7-openstack-network-in-too-much-detail-feilsoking-av-neutron-server
:status: published

Etter at en virtuell maskin har blitt startet i en instans er vi
interessert i å kunne snakke med denne maskinen utenfra OpenStack
nettverket. Det er her OpenStack in to much detail kommer inn i bildet.
 Se bildet nedenfor for mer detaljer.

|Neutron_architecture|

Jeg vil ikke prøve å forklare dette i detalj da nettverket er veldig
komplekst.
`Artikkelen <http://openstack.redhat.com/Networking_in_too_much_detail>`__ tar
utgangspunkt i å forklare arkitekturen, og hvordan nettverk, bruer og
tunneler henger sammen i en OpenStack installasjon. Bildet er forøvrig
skrevet ut og ligger ved arbeidsstasjonen min, regner med at det skal
repeteres en god del ganger før nettverket sitter 100%.

Etter at vi hadde fått laget instanser ville ikke nettverket i en
instans starte slik vi ville. Etter litt feilsøking fant vi ut at
neutron-server tjenesten på compute noden ikke starter. Tjenesten dør
momentant når den blir startet og det skjer såpass fort at det ikke er
noe innslag i loggen som kan si hva som er galt. Resten av dagen gikk
med til å feilsøke hvorfor neutron-server ikke ville starte.
Initscriptet er likt som på controller noden, og
/etc/neutron/neutron.conf er identisk på de to maskinene. Dette må
feilsøkes ytterligere, fortsettelse følger på mandag.

.. |Neutron_architecture| image:: http://openstack.b.uib.no/files/2014/08/Neutron_architecture-300x166.png
   :target: http://openstack.b.uib.no/files/2014/08/Neutron_architecture.png
