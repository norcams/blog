Dag 22: Installering av Ceph kluster
####################################
:date: 2014-10-24 06:58
:author: Kristian Skurtveit
:email:	kristian.skurtveit@gmail.com 
:category: bachelorprosjekt
:tags: ceph, RedHat, Stackforge, storage
:slug: dag-22-installering-av-ceph-kluster
:status: published

Agenda i dag var å få lest litt mer om filsystemet Ceph.
`Ceph <http://ceph.com/>`__ er et objekt basert filsystem som replikerer
sine data over et lagringskluster. Det tar vekk behovet for et
tradisjonelt SAN. Filsystemet ble utviklet i 2007, og ble i Mai i år
kjøpt opp av
`RedHat. <http://ceph.com/community/red-hat-to-acquire-inktank/>`__

I prosjektet har vi lyst å deployere Ceph ved bruk av Puppet moduler.
For å få en så knirkefri installasjon som overhodet mulig kommer vi til
å bruke samme utviklere som laget OpenStack puppet modulene vi benyttet
tidligere. Stackforge utviklerne har mye spennende GitHub prosjekter
innenfor OpenStack og dens komponenter. For de som er interessert i å
sjekke ut Ceph repositoriet kan ta en kikk
`her <https://github.com/stackforge/puppet-ceph/>`__.

I første omgang har vi deployert et Ceph kluster manuelt for å få et
innblikk i hvordan dette fungerer bit for bit før vi begynner å bruke
puppet modulene. Det er mye god dokumentasjon som ligger ute på
hjemmesidene til Ceph, vi begynte med følgende
`"quick-start-preflight" <http://docs.ceph.com/docs/master/start/quick-start-preflight/>`__. 
Deretter ble klusteret installert ved å følge
`"quick-start-deploy". <http://docs.ceph.com/docs/master/start/quick-ceph-deploy/>`__

Et kjørende kluster can for eksempel se slik ut:

|ceph-cluster|

.. |ceph-cluster| image:: http://openstack.b.uib.no/files/2014/10/ceph-cluster.png
   :target: http://openstack.b.uib.no/files/2014/10/ceph-cluster.png
