Dag 4: Videre konfigurasjon av winch
####################################
:date: 2015-03-14 23:13
:author: Kristian Skurtveit
:email:	kristian.skurtveit@gmail.com
:category: bachelorprosjekt
:tags: blade server, winch
:slug: dag-4-videre-konfigurasjon-av-winch
:status: published

Dagen ble benyttet til å teste at provisjoneringen av controller og
compute fungerer sammen med logstash. Det er mye av konfigurasjonen som
utføres manuelt for øyeblikket. Blant annet må alle OpenStack tjenestene
manuelt endres for at de skal logge til syslog og sende til logstash
noden som tar imot og parser loggende.

Førsteprioritet er uansett å få opp et fysisk testmiljø der jeg har
muligheten til å starte flere instanser og sjekke at all informasjon som
blir generert i loggfilene blir samlet og håndtert. Videre må
nøkkelfunksjonalitet i systemet testes på en slik måte at loggdataene
som blir generert kan si noe om hvilken tilstand systemet er i. Om
tjenester er oppe og går, om det har forekommet feil den siste tiden
osv.
