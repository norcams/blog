Dag 10: Feilsøking av instansnettverk & installasjon av "winch"
###############################################################
:date: 2014-09-05 10:40
:author: Kristian Skurtveit
:email:	kristian.skurtveit@gmail.com 
:category: bachelorprosjekt
:tags: foreman, iptables, winch
:slug: dag-10-feilsoking-av-instansnettverk-installasjon-av-winch
:status: published

Første del av dagen ble brukt til videre feilsøking av hvorfor
instansene våre ikke kunne snakke ut mot verden. Dette ble løst med å
spesifisere hvilket interface vi skulle kjøre maskering ifra. Iptables
regelen fra `OpenStack networking in too
much <https://openstack.redhat.com/Networking_in_too_much_detail>`__
detail ble modifisert til å se slik ut:

    iptables -t nat -I POSTROUTING 1 -s 172.24.4.224/28 -o eth0 -j
    MASQUERADE

Etter en iptables reload kunne instansene våre snakke ut mot verden.
Innenfor sine begrensede parametere kunne vi nå si at vi hadde en
fullverdig OpenStack installasjon.

Resten av dagen ble benyttet til å se på
`"winch" <https://github.com/norcams/winch>`__ prosjektet fra GitHub.
Dette er et prosjekt på lik linje med OpenStack fra scratch. Formålet
med winch er å lære oss å deployere OpenStack ved hjelp av puppet
moduler og `The Forman <http://theforeman.org/learn_more.html>`__. Kort
forklart er Forman en effektiv måte å installere all infrastruktur til
OpenStack installasjonen, eksempelvis compute, storage og network.
Foreman gir mye spennende funksjonalitet, så anbefaler videre lesning i
linken over. Når "winch" ble laget var OpenStack kommet til havana
versjonen. I disse dager bruker vi icehouse, som er samme versjon som
ble installert ved hjelp av packstack. For å kunne jobbe videre med
"winch" er vi først nødt til å oppdatere denne til å støtte icehouse.
Dette vil være klart til neste gang.

 
