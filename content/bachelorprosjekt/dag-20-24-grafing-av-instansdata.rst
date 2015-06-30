Dag 20-24: Grafing av instansdata
#################################
:date: 2015-05-04 12:58
:author: Kristian Skurtveit
:email:	kristian.skurtveit@gmail.com
:category: bachelorprosjekt
:tags: instanser, keystone, nova
:slug: dag-20-24-grafing-av-instansdata
:status: published

Etter å ha eksperimentert med ulike metrics fra Logstash og statsd i
forrige uke har jeg laget noen enkle python scripts som spør keystone
databasen ved jevne mellomrom for instansdata. Antallet kjørende
instanser, slettede instanser, instanser som har feilet, samt type
instans blir nå grafet i Grafana.

Grunnen for dette er at vi skal kunne holde en enkel oversikt over alle
instansene og deres status. I tillegg skal vi kunne kartlegge fremtidige
ressursbehov dersom totalkapasiteten i systemet er i ferd med å bli
nådd. Dette går under kategorien proaktiv overvåking, og vi kan løse
ressursbehov ved å legge til mer ressurser under drift istedenfor når
systemet har nådd sin totale kapasitet.

|metrics-grafer|

 

|instans-graf|

.. |metrics-grafer| image:: http://openstack.b.uib.no/files/2015/04/metrics-grafer.png
   :target: http://openstack.b.uib.no/files/2015/04/metrics-grafer.png
.. |instans-graf| image:: http://openstack.b.uib.no/files/2015/05/instans-graf.png
   :target: http://openstack.b.uib.no/files/2015/05/instans-graf.png
