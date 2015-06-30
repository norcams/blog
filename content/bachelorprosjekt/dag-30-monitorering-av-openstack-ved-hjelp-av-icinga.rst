Dag 30: Monitorering av OpenStack ved hjelp av Icinga
#####################################################
:date: 2014-11-21 11:13
:author: Kristian Skurtveit
:email:	kristian.skurtveit@gmail.com 
:category: bachelorprosjekt
:tags: bachelor, icinga, monitorering, nagios, openstack, overvåkning
:slug: dag-30-monitorering-av-openstack-ved-hjelp-av-icinga
:status: published

Monitorering er et stort og viktig tema innenfor OpenStack og det finnes
mange forskjellige verktøy som kan benyttes. Jeg har så vidt begynt å
kikke på `Icinga <https://www.icinga.org/>`__.

Icinga kan vise seg å være et nyttig verktøy for monitorering av
OpenStack. Verktøyet er i utgangspunktet basert på Nagios, derfor kan
mange av tilleggene som var skrevet for Nagios brukes direkte i Icinga.
For eksempel har
`Stackforge <https://github.com/stackforge/monitoring-for-openstack>`__
en rekke scripts som kan brukes for å overvåke rene OpenStack tjenester.

Samtidig har utviklerne bak Icinga støtte for å installere verktøyet ved
hjelp av puppet moduler, og tilbyr også vagrant bokser til testformål.
Siden resten av IaaS plattformen gjør dette per dags dato er Icinga
absolutt interessant å ha med videre som et aktuelt verktøy.
