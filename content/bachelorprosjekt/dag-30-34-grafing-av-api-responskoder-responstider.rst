Dag 30-34: Grafing av API responskoder & responstider
#####################################################
:date: 2015-05-21 11:26
:author: Kristian Skurtveit
:email:	kristian.skurtveit@gmail.com
:category: bachelorprosjekt
:tags: api responskoder, prosjektrapport
:slug: dag-30-34-grafing-av-api-responskoder-responstider
:status: published

Siden vi allerede ekstraherer alle loggmeldinger som genereres i
OpenStack kan vi også hente ut og visualisere API-responskoder og
API-responstider.  Dette grafes på følgende måte: |api-responses|

Med en API responstid følger også en responskode.  For å  se hvor mange
ganger responskodene forekommer i forhold til hverandre kan dette
visualiseres på denne måten:

|total api-response-codes|

Etter helgen 17. mai vil jeg hovedsaklig fokusere på å fullføre et
utkast til prosjektrapporten som skal inn den 26. mai. Endelig
innleveringsfrist er satt til 9 juni og prosjektrapporten vil
selvfølgelig bli publisert på bloggen.

.. |api-responses| image:: http://openstack.b.uib.no/files/2015/05/api-responses.png
   :target: http://openstack.b.uib.no/files/2015/05/api-responses.png
.. |total api-response-codes| image:: http://openstack.b.uib.no/files/2015/05/total-api-response-codes.png
   :target: http://openstack.b.uib.no/files/2015/05/total-api-response-codes.png
