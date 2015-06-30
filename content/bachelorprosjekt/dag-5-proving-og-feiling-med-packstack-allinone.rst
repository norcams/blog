Dag 5: Prøving og feiling med packstack --allinone
##################################################
:date: 2014-08-21 18:11
:author: Kristian Skurtveit
:email:	kristian.skurtveit@gmail.com 
:category: bachelorprosjekt
:tags: centos, openstack, packstack, rdo
:slug: dag-5-proving-og-feiling-med-packstack-allinone
:status: published

15 august. De tre hovedkomponentene til OpenStack hadde nå blitt
installert med packstack til å kjøre på en og samme node.  Dette burde
ikke by på store problemer da RDO pakken fra Red Hat er godt testet og
fungerer i mange installasjoner av OpenStack der ute i dag.

Alle instanser som kjører innad i OpenStack rammeverket kan
administreres via et webpanel kalt
`Horizon <https://wiki.openstack.org/wiki/Horizon>`__. Panelet gir en
god oversikt over antall instanser, deres ressursbruk, last, og annen
info. På sikt skal både administratorer og vanlige brukere kunne logge
seg inn her og administrere sine egne maskiner til forskjellige formål.
Et lite utdrag fra Horizon:

|Horizon-overview|

Vi fikk fortsatt problemer med å lage og starte instanser med å kjøre de
tre hovedkomponentene på en og samme node. Mistenker at dette kan ha med
lite tilgjengelige ressurser siden vi kjører på en virtuell maskin
gjennom VirtualBox. For å løse denne problematikken ble svaret å lage en
ekstra compute node på en fysisk maskin. Med dette ville vi unngå
problematikken vi hadde hatt til nå, i tillegg til at vi kan lage flere
maskiner siden vi har mer ressurser tilgjengelig.

For å installere en egen compute node trenger man, (i vårt tilfelle) en
nyinstallert `CentOS <http://en.wikipedia.org/wiki/CentOS>`__ samt
packstack-answer filen vi brukte når vi installerte hoved noden. Da vil
packstack bruke de samme passordene til de ulike komponentene og compute
noden vil peke tilbake til controller noden slik at disse vil snakke
sammen.

Mye av installasjon av compute noden er lik som forrige gang. Når alt i
konfigurasjonsfilen er klart blir det kjørt på samme måte som tidligere
med en liten endring. Istedenfor:

::

    packstack --allinone

Blir det nå spesifisert en svarfil som brukes i installasjonen:

    ::

        packstack --answer-file=$youranswerfile

.. |Horizon-overview| image:: http://openstack.b.uib.no/files/2014/08/Horizon-overview-300x132.png
   :target: http://openstack.b.uib.no/files/2014/08/Horizon-overview.png
