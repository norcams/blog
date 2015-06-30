Dag 8: Videre feilsøking av neutron-server
##########################################
:date: 2014-08-28 08:34
:author: Kristian Skurtveit
:email:	kristian.skurtveit@gmail.com 
:category: bachelorprosjekt
:tags: compute, controller, feilsøking, openstack, plugin
:slug: dag-8-videre-feilsoking-av-neutron-server-og-installasjon-av-fysisk-controller-node
:status: published

På denne dagen gikk mye av tiden med til å feilsøke hvorfor
neutron-server ikke ville starte på compute noden. Feilsøking uten å ha
noe logg å lese kan ofte være vanskelig, og da kommer det helt an på
hvilke svar man kan finne på nettet i lignende installasjoner. Til slutt
viste det seg at en av de tilleggene som neutron bruker ikke fantes på
den stien den skulle ha vært, og tillegget var heller ikke installert.

::

    yum install openstack-neutron-ml2

I tillegg skal det være en plugin.ini fil under /etc/neutron/ som skal
holde rede på hvilke tillegg man har lagt til installasjonen av
OpenStack. Denne må symlinkes hertil.

::

    ln -s /etc/neutron/plugins/ml2/ml2_conf.ini /etc/neutron/plugin.ini

Etter dette fungerte det å starte neutron-server tjenesten. Foruten om
dette har det vært noen stabilitetsproblemer på controller noden. Denne
har til nå kjørt på en virtuell maskin og har flere ganger fått økt
minnetildeling. I skrivende stund kjører den på 4GB RAM, halvparten av
det jeg har på min arbeidsstasjon. Jeg har opptil flere ganger hatt
stabilitetsproblemer ved å kjøre denne maskinen virtuelt. En del ganger
har jeg blitt nødt til å kjøre power down eller reset for å få kontakt
med maskinen. På grunn av dette er planen til neste gang å få lagt
controller noden over på en fysisk maskin. Samtidig skal vi også
installere ML2 tillegget før vi kjører packstack, slik at vi ikke får de
samme problemene med neutron-server som tidligere.

 

 
