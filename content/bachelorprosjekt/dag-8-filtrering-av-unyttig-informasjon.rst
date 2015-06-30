Dag 8: Filtrering av unyttig informasjon
########################################
:date: 2015-03-31 20:08
:author: Kristian Skurtveit
:email:	kristian.skurtveit@gmail.com
:category: bachelorprosjekt
:tags: grok, logstash, regulære uttrykk
:slug: dag-8-filtrering-av-unyttig-informasjon
:status: published

Ikke alle data som kommer inn gjennom Logstash er nyttige data. Data som
ikke gir noen nyttig informasjon eller rett og slett bare er støy er
nødt til å skjules eller filtreres bort. I Logstash kan alle datafelter
som blir opprettet når man lager filter søkes i. På bakgrunn av dette
kan man ved hjelp av regulære uttrykk søke etter informasjon man vil
filtrere bort slik at dette ikke kommer med. Hvis man for eksempel ikke
skulle ønske å se alle infomeldinger som et system genererer kan dette
filtreres bort på denne måten.

+--------------------------------------------------------------------------+
| if "INFO" in [openstack\_loglevel] {drop {}                              |
|                                                                          |
| .. raw:: html                                                            |
|                                                                          |
|    </p>                                                                  |
|                                                                          |
| .. raw:: html                                                            |
|                                                                          |
|    <p>                                                                   |
|                                                                          |
| }                                                                        |
+--------------------------------------------------------------------------+
+--------------------------------------------------------------------------+

Videre vil jeg ta en fullstendig gjennomgang av hva informasjon som skal
filtreres bort slik at dette ikke overskygger viktige data i henhold til
problemstillingen.

 

 
