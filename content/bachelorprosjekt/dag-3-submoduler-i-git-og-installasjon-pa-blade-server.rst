Dag 3: Submoduler i git og installasjon på blade server
#######################################################
:date: 2015-03-14 21:45
:author: Kristian Skurtveit
:email:	kristian.skurtveit@gmail.com
:category: bachelorprosjekt
:tags: logstash, puppet, rsyslog
:slug: dag-3-submoduler-i-git-og-installasjon-pa-blade-server
:status: published

I forrige uke fikk jeg problemer med å legge til enkelte puppetmoduler
til monitoreringsbranchen på github. Etter en del feilsøking endte jeg 
opp med å legge disse til som submoduler. Fordelen med submoduler er at
man slipper å måtte oppdatere modulene i sitt eget repository. Ved å
kjøre kommandoen nedenfor vil modulen lastes ned, og det vil ligge en
sti til det remote repositoriet i .gitmodules.

::

    git submodule add https://github.com/elastic/puppet-logstash

I tillegg til submodulene er det også blitt lagt til en egen mappe for
alle konfigurasjonsfiler og patterns til logstash. Rsyslog.conf ligger
også her, men planen videre er å legge til rsyslog puppetmodulen slik at
det aller meste kan styres gjennom puppet. Jeg begynte også å installere
winch på blade serveren jeg har fått tildelt. Denne serveren har 32GB
med minne og jeg har derfor mulighet til å ha kjørende en god del
instanser som jeg skal teste med. Mer om dette i morgen!
