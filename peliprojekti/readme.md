# Project α

## Pelin idea

Project α ideana on olla tekstipohjainen seikkailupeli, jossa pelaaja osti halvalla vanhan hylätyn talon. Pelin ideana on, että pelaaja kerää roskia ympäri taloa ja kierrättävät nämä oikein. Kun kaikki roskat on löydetty ja kierrätetty, niin peli loppuu. Jonka jälkeen pelaaja saa lopullisen pistemäärän ja muuttuvan tekstin riippuen siitä miten hyvin he tekivät roskien lajittelun.

Pelissä on myöskin hyvin alkeellinen pulma, jossa pelaaja ei pääse menemään varastoon ilman taskulamppua. Peli kertoo tästä pelaajalle jos he sit koittavat tehdä.
Tämä taskulamppu myös tarvitsee pariston, josta myöskin kerrotaan pelaajalle, jos he koittavat mennä varastoon pelkän taskulampun kanssa.

## Toimintaperiaate

Ohjelman käynnistyessä kysytään nimi, jonka jälkeen pelaaja sijoitetaan pelin ensimmäiseen huoneeseen (eteinen/entryway). Pelaaja voi valita valikosta eri toimintoja:

- liikkua huoneesta toiseen
- kerätä huoneessa olevat esineet/roskat
- tarkastella mukana olevia esineitä/roskia
- tarkastella nykyistä sijaintia ja huoneen kuvausta
- kierrättää roskia (eteisessä)
- lopettaa pelin (joka tallentaa pelin)

Pelaaja, huoneet ja esineet ovat omia luokkiaan, joiden avulla pelin eri osat voidaan pitää erillään ja niitä voidaan kehittää itsenäisesti.

## Projektin rakenne

'pelaaja' kansio sisältää 'Pelaaja'-luokan. Pelaajalla on nimi, sijainti sekä lista kerätyistä esineistä.

'huone' kansio sisältää 'Huone'-luokan. Huoneella on nimi, kuvaus ja mahdollinen esine.

'esine' kansio sisältää 'Esine'-luokan. Esineellä on nimi ja paino.

'main.py' sisältää ohjelman käynnistyksen sekä pelin päävalikon.

## Kestävä kehitys

Koodi on jaettu pieniin ja selkeästi määriteltyihin luokkiin ja tiedostoihin, mikä tekee ohjelmasta helpommin ylläpidettävän ja laajennettavan. Näin samoja rakenteita voidaan hyödyntää myöhemmin ilman, että koko ohjelmaa tarvitsee tehdä uudelleen.
Tämä periaatteessa kestävää kehitystä(?)

Pelin tarina on se että pelaaja osti halvalla talon joka oli muuten hylätty.
Ja ideana on nyt siivota ja kierrättää roskia mitä pelaaja löytää talon sisältä.
Tämä ymmärtääkseni sopii oikein hyvin tähän kestävän kehityksen näkökulmaan.


V 1.1.0 - Pelin "foundation" tehty.

V 1.1.1 - Pelin koodi koitettu muuttaa selvemmäksi, ja samalla lisätty "tallennus" toiminto. Jotta pelaaja voi jatkaa samasta kohdasta mihin jätti pelin. 
Lisätty myös intro.txt ja ohjeet.txt

V 2.0.0 - Peli on nyt valmis. Tai ainakin pitäisi olla valmis. Peliin on lisätty lajittelu mini peli, ja pieni pulma, jossa et pääse varastoon ilman tasklumappua. Tämä taskulamppu myös tarvitsee pariston.