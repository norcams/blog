Dag 23: Installering av Ceph kluster med hjelp av puppet-moduler
################################################################
:date: 2014-10-30 13:15
:author: Kristian Skurtveit
:email:	kristian.skurtveit@gmail.com 
:category: bachelorprosjekt
:slug: dag-23-installering-av-ceph-kluster-med-hjelp-av-puppet-moduler
:status: published

Det manuelle oppsettet av ceph-klusteret som ble installert forrige gang
fungerte bra. Planen for i dag var å lage et lignende kluster ved hjelp
av puppet moduler.

Som vi husker fra tegningen jeg publiserte i forrige innlegg, fantes det
en egen monitoreringsnode og x antall osd noder. Ceph klusteret blir
spredt over alle osd nodene. Mens det er en monitoreringsnode som holder
styr på `klusteret <http://ceph.com/docs/master/architecture/>`__ og
hvor mange noder som er med osv.  For å hindre
`SPOF <http://en.wikipedia.org/wiki/Single_point_of_failure>`__ har vi i
et produksjonsmiljø lyst å kjøre flere monitoreringsnoder samtidig. I
tillegg ønsker vi å kjøre monitoreringsnoder og osd noder på samme
maskin. Dette for å minske behovet for ekstra maskiner.

I node definisjonen i vagrant har vi lagt til 3 ceph noder; ceph01,
ceph02 og ceph03. Innstillinger for de 3 maskinene har blitt satt i
`common.yaml <https://github.com/norcams/winch/blob/ceph/puppet/hieradata/common.yaml>`__
filen slik at vi kan provisjonere med puppet. Innstillingene til ceph
inneholder alt fra passord, medlemmer  på klusteret, størrelsen til
klusteret og hvor klusteret skal være på de medlemmene som er definert.
Dette vil nå bli satt opp automatisk for oss når vi installerer ceph
nodene.

Etter dette kunne vi starte opp maskinene på samme måte som vi har gjort
tidligere. Klusteret innstalleres når maskinen kommer opp for første
gang. Mer om ceph neste gang.

 
