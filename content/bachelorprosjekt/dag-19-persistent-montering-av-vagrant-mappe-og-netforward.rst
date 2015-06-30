Dag 19: Persistent montering av /vagrant/ mappe og netforward
#############################################################
:date: 2014-10-13 06:41
:author: Kristian Skurtveit
:email:	kristian.skurtveit@gmail.com 
:category: bachelorprosjekt
:tags: github, openstack, vagrant
:slug: dag-19-persistent-montering-av-vagrant-mappe-og-netforward
:status: published

Som tidligere nevnt har det vært problemer ved bruk av vagrant at vi
mister /vagrant mappen på manager maskinen. I denne mappen ligger det en
del script for å installere og konfigurere Foreman og puppet. Da er det
veldig viktig at montering av denne mappen fungerer i alle tilfeller der
vi trenger den.

Ved bruk av vagrant har dette vist seg å være vanskelig. Etter en
oppdatering av maskinen eller en restart utenfor vagrant miljøet blir
man tvunget til å kjøre kompilering av virtualbox addons og
kjernemoduler for å få monteringen opp igjen. Dette krever mye manuelt
arbeid og det ville vært lettere å automatisert prosessen. Derfor har
jeg laget et script som ordner dette. I tillegg til å montere mappen
kjører den også netforward på manager maskinen. Denne har tidligere falt
ut når manager har blitt startet om utenfor vagrant og er kritisk for at
Foreman fungerer slik vi vil.

Scriptet kan sees i sin helhet på
`github <https://github.com/norcams/winch/blob/master/vagrant/manager-persistent-config.sh>`__.
