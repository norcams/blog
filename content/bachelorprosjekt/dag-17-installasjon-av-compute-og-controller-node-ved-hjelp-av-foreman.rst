Dag 17: Installasjon av compute og controller node ved hjelp av Foreman
#######################################################################
:date: 2014-10-02 10:43
:author: Kristian Skurtveit
:email:	kristian.skurtveit@gmail.com 
:category: bachelorprosjekt
:tags: foreman, puppet, winch
:slug: dag-17-installasjon-av-compute-og-controller-node-ved-hjelp-av-foreman
:status: published

Vi fortsatte med feilsøkingen fra fredag om hvorfor puppet modulene fra
"winch" ikke ville fungere når vi provisjonerte med Foreman. De hadde
virket før og det ga lite mening at de ikke skulle virke nå som Foreman
var med i bildet.

Det viste seg at feilen lå spredt i flere konfigurasjonsfiler, og dette
gjorde at puppet modulene feilet på maskinene som Foreman installerte.
Nå har det blitt gjort endringer i kickstart filene til Foreman for å
gjøre at dette problemet ikke vil oppstå igjen. Nå var det mulig å
installere både controller og compute noder ved hjelp av Foreman der
alle puppet modulene blir installert.

Til nå har vi brukt vagrant og virtualbox for å lage og provisjonere
maskiner. Vagrant legger opp et eth0 interface med en NAT adresse, men
dette kludrer mye til det nettverksoppsettet vi ønsker. Derfor er neste
steg nå å lage install script som kan lage og sette opp virtualbox
maskiner for å unngå at eth0 inferfacet blir bundet opp til denne NAT
adressen. Mer om dette på fredag.
