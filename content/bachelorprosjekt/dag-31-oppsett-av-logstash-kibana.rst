Dag 31: Logstash & Kibana
#########################
:date: 2014-11-26 07:04
:author: Kristian Skurtveit
:email:	kristian.skurtveit@gmail.com 
:category: bachelorprosjekt
:tags: elasticsearch, graphite, kibana, logging
:slug: dag-31-oppsett-av-logstash-kibana
:status: published

Benyttet mesteparten av dagen til å kikke på to verktøy som heter
`Logstash <gstash.net>`__\ og
`Kibana <http://www.elasticsearch.org/overview/kibana/>`__. Logstash er
et verktøy for å samle og håndtere logg. Den samler inn, parser og
lagrer logg og viser dem i et webpanel kalt Kibana. Her kan man ved
hjelp av et kraftig søkeverktøy søke opp alt av hendelser som har skjedd
på systemet siden loggingen startet. I webpanelet vil det genereres
grafer på hvor ofte en hendelse man har søkt på forekommer. Ganske
nyttig dersom man skal filtrere en spesifikk feil for å finne ut om
feilen er kritisk eller ikke.

Konfigurasjonsmessig kan man gjøre mye med logstash. Det viktigste av
konfigurasjonen skjer ved hjelp av en konfigurasjonsfil der en
spesifiserer input, hva som skal filtreres og output. Output delen kan
være forskjellige tjenester, i dette tilfellet ble output satt til å
være elasticsearch. Elasticsearch er logstash' sin backend for lagring
av logg. Senere vil jeg ta for meg installasjonen og oppsett av logstash
og kartlegge tjenester som skal overvåkes. I tillegg ønsker jeg også å
kikke nærmere på verktøyet
`Graphite <http://graphite.wikidot.com/>`__ som kan spesifiseres som
output.
