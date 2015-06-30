Dag 6: Installering av fysisk compute node
##########################################
:date: 2014-08-22 18:24
:author: Kristian Skurtveit
:email:	kristian.skurtveit@gmail.com 
:category: bachelorprosjekt
:tags: compute, horizon, openstack
:slug: dag-6-installering-av-fysisk-compute-node
:status: published

18. august hadde vi fått installert compute noden på en fysisk maskin.
Til nå hadde vi hatt problemer med å lage og starte instanser når alt
kjørte på en node, på grunn av lite tilgjengelige ressurser. Som
tidligere forklart kunne vi nå bruke packstack svarfilen som ville gjøre
installsjonen for oss. Det eneste man oppgir er root passordet til
maskinen man skal installere på.

    \*\*\*\* Installation completed successfully \*\*\*\*\*\*

Etter installasjonen får man oppgitt adressen til
`Horizon <https://wiki.openstack.org/wiki/Horizon>`__ der man kan logge
inn og administrere skyen. På dette tidspunktet klarte vi å logge inn og
lage instanser.

|lage-instans|

Det er de tilgjengelige ressursene man har på compute noden som vil
sette begrensninger på hvor mange instanser man kan lage. Man kan velge
størrelse på maskinen og hvor mange instanser av maskinen som skal
starte. Utifra de verdiene man spesifiserer vil ressursene under project
limits endre seg. I verktøyet kan man spesifisere sikkerhet, hva
nettverk maskinen skal ha, hva post-scripts som skal kjøres og om man
vil kjøre automatisk eller manuelt diskoppsett. Alt i alt er det et
veldig oversiktlig og funksjonelt verktøy som det skal bli veldig kjekt
å lære mer om!

 

.. |lage-instans| image:: http://openstack.b.uib.no/files/2014/08/lage-instans-300x274.png
   :target: http://openstack.b.uib.no/files/2014/08/lage-instans.png
