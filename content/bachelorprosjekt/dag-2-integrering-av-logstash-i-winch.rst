Dag 2: Integrering av logstash i "winch"
########################################
:date: 2015-03-07 16:56
:author: Kristian Skurtveit
:email:	kristian.skurtveit@gmail.com
:category: bachelorprosjekt
:tags: github, logstash, puppet, winch
:slug: dag-2-integrering-av-logstash-i-winch
:status: published

Under utplasseringen var jeg med på å lage et automatisk oppsett som
installerte OpenStack og tilhørende komponenter. Dette ble gjort ufifra
et prosjekt på github som het
`winch <https://github.com/norcams/winch>`__. Som jeg tok opp i min
forrige bloggpost ønsker jeg å samle alle OpenStack loggene på en og
samme maskin. Derfor her jeg laget en ny branch i winch som inkluderer
en monitoreringsnode. Denne noden vil være ansvarlig for alt som skjer
med tanke på logginnsamling, parsing og visualisering av informasjon. Da
er det viktig at verktøyene som skal gjøre dette blir installert på
samme måte som tidligere, ved hjelp av puppetmoduler.  Da kan vi sette
en ønsket tilstand og si at den nye noden skal være en
monitoreringsnode.

Arbeidet med å puppetifisere alle verktøyene er kommet godt i gang. Har
laget en manifest fil for logstash som kan sees
`her <https://github.com/norcams/winch/blob/stable/icehouse-centos6-monitoring/puppet/manifests/logstash.pp>`__.
Denne vil benytte seg av puppet modulene lokalisert i puppet/modules og
installere verktøyene med konfigurasjonsfiler spesifisert i manifestet.
Det som gjenstår for at integreringen skal være komplett er å legge til
de puppetmodulene jeg trenger. Disse er submoduler og blir derfor lagt
til annerledes. Mer om dette i neste bloggpost.
