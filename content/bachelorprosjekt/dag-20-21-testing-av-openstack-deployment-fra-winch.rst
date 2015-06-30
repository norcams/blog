Dag 20 & 21: Testing av Openstack deployment fra "winch"
########################################################
:date: 2014-10-17 20:53
:author: Kristian Skurtveit
:email:	kristian.skurtveit@gmail.com 
:category: bachelorprosjekt
:tags: ceph, openstack, storage, winch
:slug: dag-20-21-testing-av-openstack-deployment-fra-winch
:status: published

I den siste tiden har det skjedd flere endringer på
`"winch" <https://github.com/norcams/winch>`__ prosjektet på Github. Vi
har nå et automatisert testmiljø som kan installere OpenStack og alle
dens komponenter uten å måtte sette mange innstillinger manuelt.  Dette
gir oss stort spillerom dersom noe ikke skulle virke med senere
anledninger. Da kan vi slette en komponent og installere den på nytt
igjen uten å tape mye tid.

Samtidig vil det være lettere å lære seg de ulike OpenStack komponentene
når man kan se hvordan de fungerer sammen i praksis. Det er  lett å
miste oversikten når man begynner med rammeverket siden det virker
veldig overveldende og detaljert i starten.

Dagens arbeid innebærte en god del testing, samt en endring i en av
installasjonsfilene. Vi kan nå konkludere med at "winch" er brukbart i
forhold til de tingene vi skal gjøre videre. Blant annet skal vi kikke
nærmere på storage, rettere sagt `Ceph <http://ceph.com/>`__.

 

 
