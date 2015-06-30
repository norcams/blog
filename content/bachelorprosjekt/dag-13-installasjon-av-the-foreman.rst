Dag 13: Installasjon av The Foreman
###################################
:date: 2014-09-15 06:16
:author: Kristian Skurtveit
:email:	kristian.skurtveit@gmail.com 
:category: bachelorprosjekt
:tags: foreman, openstack, provisjonering, winch
:slug: dag-13-installasjon-av-the-foreman
:status: published

Etter å ha fått "winch" oppgradert til siste OpenStack versjon; Icehouse
started vi med installasjonen av `The
Foreman. <http://theforeman.org/>`__\ Foreman ligger inne i "winch" med
versjon 1.4.5 og formålet med å installere denne versjonen er å kunne
verifisere at funksjonaliteten fungerer slik vi vil. Senere vil Foreman
bli oppgradert til versjon 1.6.0 .

Foreman vil være en egen komponent i vår OpenStack installasjon og den
kjører derfor på en egen maskin, nemlig manager. Før installasjon av
Foreman må denne maskinen ha blitt laget. Inne i vagrant mappen på
`winch <https://github.com/norcams/winch/blob/foreman/vagrant/foreman.sh>`__\ finnes
det et script som heter foreman.sh. Det er dette scriptet som kjøres når
Foreman installeres.

Etter installasjon skjer alt av administrasjon inne fra et webpanel. Her
kan man sette opp puppet moduler, templater for installasjon og
provisjonering, diskoppsett med mer. Det finnes mange muligheter, og det
er dette verktøyet vi skal bruke i lag med OpenStack. Eksempelvis om man
skulle installere 40 servere ville man konfigurert Foreman til å gjøre
dette på en rask og effektiv måte. Alternativt måtte man gjort dette for
hver og enkelt server noe som ikke skalerer i lengden. På mandag vil vi
jobbe videre med The Foreman og sette igang med provisjonering av
compute noder.

 
