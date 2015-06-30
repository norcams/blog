Dag 3: Videre feilsøking av OpenStack from scratch
##################################################
:date: 2014-08-20 11:59
:author: Kristian Skurtveit
:email:	kristian.skurtveit@gmail.com 
:category: bachelorprosjekt
:tags: feilsøking, glance, nova, ofs
:slug: dag-3-videre-feilsoking-av-openstack-from-scratch
:status: published

8. august gikk mye av tiden til å feilsøke på hvorfor installasjonen fra
gårsdagen ikke ville lage instanser.  OpenStack from scratch har en
rekke tester en kan kjøre når installasjonen er ferdig. Testene ligger
her: \ https://github.com/norcams/ofs/tree/master/tests

For eksempel vil
`import\_image.sh <https://github.com/norcams/ofs/blob/master/tests/01-import_image.sh>`__ importere
et image som den virtuelle maskinen i instansen vil starte fra. Dette
for å verifisere at glance image service fra OpenStack fungerer som det
skal. I vårt tilfelle feilet
`04-boot.sh <https://github.com/norcams/ofs/blob/master/tests/04-boot.sh>`__ som
bruker komponenten nova til å starte den virtuelle maskinen. Det ble
etterhvert mye lesing i nova loggene for å finne ut av feilen. Jeg hadde
funnet frem til flere alternative løsninger fra nettet for å gjøre ting
i en annen rekkefølge. Samt at jeg reinstallerte de tre
 hovedkomponentene network storage og compute for å teste ut noen av
løsningene. Dette ga ikke noen resultater.

Det har uansett vært interessant å ha installert dette fra bunnen av,
selv om vi visste på forhånd at det ville være noen feil med
installasjonen. Jeg har blitt fortrolig med flere av kommandoene på de
verktøyene som er i bruk samtidig som jeg har fått et greit overblikk på
hvordan komponentene fungerer sammen. I neste uke har vi tenkt å gå
videre med en annen installasjon av OpenStack
nemlig \ `RDO <http://openstack.redhat.com/Frequently_Asked_Questions#What_is_RDO.3F>`__.

 

 

 
