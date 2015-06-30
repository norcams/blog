Dag 4: Installasjon av OpenStack packstack
##########################################
:date: 2014-08-21 10:58
:author: Kristian Skurtveit
:email:	kristian.skurtveit@gmail.com 
:category: bachelorprosjekt
:tags: centos, fedora, openstack, packstack, rdo, rhel
:slug: dag-4-installasjon-av-openstack-packstack
:status: published

11. august var satt av til å installere OpenStack fra RDO. RDO er under
utvikling av Red Hat og er en egen utgivelse av OpenStack laget
spesifikt for å kjøre
på \ `RHEL <http://en.wikipedia.org/wiki/Red_Hat_Enterprise_Linux>`__,
`CentOS <http://en.wikipedia.org/wiki/CentOS>`__, \ `Fedora <http://en.wikipedia.org/wiki/Fedora_(operating_system)>`__ og
andre Red Hat baserte systemer.  For mer info om RDO vennligst se
`her <http://openstack.redhat.com/FAQ>`__.

Installasjon av RDO foregår ved hjelp av packstack. Packstack er et
installasjonsverktøy som bruker Puppet moduler for å installere
OpenStack på kompatible maskiner nevnt ovenfor. Har i denne posten valgt
å ta med steg-for-steg installasjonen av RDO for å vise hvordan dette
gjøres, se nedenfor for mer detaljer.

Vanligvis består OpenStack av tre hovedkomponenter; network, storage og
compute, som hver kjører på sin egen maskin. Når man installerer
packstack kan man velge at disse tre hovedkomponentene skal installeres
på en og samme maskin. Dette kan være praktisk av flere grunner, i vårt
tilfelle er det greit for å se hvordan det fungerer for testformål. Vi
kan senere også velge å separere hovedkomponentene slik vi ønsker.

RDO installeres med **3** steg. Hentet
fra \ http://openstack.redhat.com/Quickstart

**Steg 1: Programvare repository:**

Oppdater nåværende pakker på systemet:

    ::

        sudo yum update -y

Sett opp RDO repositoriet:

    ::

        sudo yum install -y http://rdo.fedorapeople.org/rdo-release.rpm

**Steg 2: Installer packstack**

    ::

        sudo yum install -y openstack-packstack

Steg 3: Kjør packstack for å installere OpenStack

Packstack installerer automatisk OpenStack slik at man slipper å
gjøre denne jobben manuelt. For å kjøre OpenStack på en enkelt node kan
vi som tidligere nevnt kjøre denne kommandoen:

    ::

        packstack --allinone

Etter installering vil packstack også generere en packstack-answer fil
med passord og innstillinger som den bruker under installasjon. Denne
kan så brukes om igjen til nye installasjoner eller til å lage nye noder
med samme innstillinger. Om man installerer på andre maskiner vil man
bli bedt om root passordet til maskinen før installasjonen starter.

Etter installasjon vil man kunne logge inn på panelet
`Horizon <https://wiki.openstack.org/wiki/Horizon>`__\ for å starte og
administrere de instanser man måtte ønske. Mer om dette videre.

 
