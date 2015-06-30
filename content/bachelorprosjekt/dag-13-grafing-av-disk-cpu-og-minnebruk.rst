Dag 13: Grafing av disk, cpu og minnebruk
#########################################
:date: 2015-04-17 12:04
:author: Kristian Skurtveit
:email:	kristian.skurtveit@gmail.com
:category: bachelorprosjekt
:tags: graphite, logstash, metrics
:slug: dag-13-grafing-av-disk-cpu-og-minnebruk
:status: published

Metrics til graphite blir sendt på et spesifikt format. Dette er
standard uansett hva system man bruker for å lage metrics.  Her
spesifiseres først navnet, deretter verdien og til slutt datoen.
Eksempelvis:

::

    echo "test.bash.stats 42 `date +%s`" | nc graphite.example.com 2003

Dette vil ikke gi et stort utslag på en graf, men når man sender data
over tid vil man på sikt kunne se at det gir utslag. Siden logstash
konfigurasjonen henter informasjon om disk, cpu- og minnebruk fra
loggfilene kan dette sendes videre for visualisering. Bildet under er
visualiserte data basert på denne
`konfigurasjonen <http://paste.debian.net/167281/>`__.

|metrics-grafer|

Bildet viser tre bokser som visualiserer tilgjengelige ressurser.
Diskboksen er også konfigurert slik at den endrer farge basert på hvor
mye diskplass som er tilgjengelig på disken. Dette er en god begynnelse!
I morgen og ut i neste uke kommer jeg til å fortsette med datainnsamling
og filtere i Logstash. Følg med!

.. |metrics-grafer| image:: http://openstack.b.uib.no/files/2015/04/metrics-grafer.png
   :target: http://openstack.b.uib.no/files/2015/04/metrics-grafer.png
