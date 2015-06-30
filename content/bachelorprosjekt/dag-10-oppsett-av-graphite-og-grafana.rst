Dag 10: Oppsett av Graphite og Grafana
######################################
:date: 2015-04-14 12:47
:author: Kristian Skurtveit
:email:	kristian.skurtveit@gmail.com
:category: bachelorprosjekt
:tags: grafana, logstash, puppet, winch
:slug: dag-10-oppsett-av-graphite-og-grafana
:status: published

Logstash, Kibana og Elasticsearch kjører per i dag på en egen node i
winch. For at lasten ikke skal bli for stor på denne virtuelle noden
hadde jeg i første omgang tenkt å lage en ny node for
grafvirtualisering. Grafnoden skal kjøre verktøyet Graphite, som støtter
metrics som kommer fra Logstash. I tillegg skal vi benytte oss av en
annen frontend enn det Graphite tilbyr og derfor skal også verktøyet
Grafana installeres.

Jeg benytter meg av puppetmodulene til
`echocat <https://github.com/echocat?utf8=%E2%9C%93&query=puppet->`__
siden disse er godt vedlikeholdte og konfigurasjonen av puppetkoden var
rett fram. Det meste gikk greit for seg og vagrantboksen har en
oppstart- og installasjonstid på mellom 3 og 4 minutter.  For de som er
interessert i å se litt på koden og øvrige detaljer rundt oppsettet av
vagrantboksen kan ta en kikk på
`winch <https://github.com/norcams/winch/blob/stable/icehouse-centos6-monitoring/puppet/manifests/graphite.pp>`__
repoet.

|provision-graphite|

.. |provision-graphite| image:: http://openstack.b.uib.no/files/2015/04/provision-graphite.png
   :target: http://openstack.b.uib.no/files/2015/04/provision-graphite.png
