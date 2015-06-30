Dag 7: Filtrering av instanshendelser
#####################################
:date: 2015-03-31 19:49
:author: Kristian Skurtveit
:email:	kristian.skurtveit@gmail.com
:category: bachelorprosjekt
:tags: elasticsearch, logstash, neutron
:slug: dag-7-filtrering-av-instanshendelser
:status: published

Dagen ble benyttet til å lage grok-filtre som henter ut informasjon fra
OpenStack-instanser. Om en instans blir opprettet, slettet, rebootet,
re-initialisert, utvidet eller skulle få en feil vil dette bli truffet
av filteret og vi vil kunne se denne hendelsen og all informasjon i
webpanelet Kibana.

|logstash-output|

Her ser vi at all informasjon som jeg publisert i forrige bloggpost har
kommet inn som egne felter. Disse kan nå søkes opp i og en kan
visualisere dette på forskjellige måter. Neste steg blir å se på andre
data i OpenStack og hvordan vi kan hente ut informasjon om opprettelser
av eksempelvis nettverk og rutere.

.. |logstash-output| image:: http://openstack.b.uib.no/files/2015/03/logstash-output-300x129.png
   :target: http://openstack.b.uib.no/files/2015/03/logstash-output.png
