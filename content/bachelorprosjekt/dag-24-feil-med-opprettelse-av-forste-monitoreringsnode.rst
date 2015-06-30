Dag 24: Feil med opprettelse av første monitoreringsnode
########################################################
:date: 2014-11-05 19:23
:author: Kristian Skurtveit
:email:	kristian.skurtveit@gmail.com 
:category: bachelorprosjekt
:tags: ceph, storage, winch
:slug: dag-24-feil-med-opprettelse-av-forste-monitoreringsnode
:status: published

Ved opprettelse av første monitoreringsnode, ceph01 feiler kjøringen av
puppet modulene. Fra det manuelle oppsettet lærte vi at den første noden
setter inn nøkler og passord på de andre nodene i klusteret.

*Error:
/Stage[main]/Ceph::Profile::Mon/Ceph::Key[client.bootstrap-osd]/Exec[ceph-injectkey-client.bootstrap-osd]/*

Når de to andre nodene ceph02 og ceph03 blir provisjonert så skjer ikke
denne feilen. Ting kan tyde på at nodene er svært avhenige av hverandre
når de skal provisjoneres. Ceph01 kan deretter provisjoneres på nytt
etter at andre og tredje node er kommet på. Da fungerer det uten
problemer og vi kan se utifra ceph -status at vi har et aktivt og
kjørende kluster.

    cluster 4b5c8c0a-ff60-454b-a1b4-9747aa737d19
    health HEALTH\_WARN clock skew detected on mon.ceph02, mon.ceph03
    monmap e2: 3 mons at
    {ceph01=172.16.33.13:6789/0,ceph02=172.16.33.14:6789/0,ceph03=172.16.33.15:6789/0},
    election epoch 6, quorum 0,1,2 ceph01,ceph02,ceph03
    osdmap e17: 6 osds: 6 up, 6 in
    pgmap v24: 192 pgs, 3 pools, 0 bytes data, 0 objects
    68720 MB used, 149 GB / 227 GB avail
    192 active+clean

