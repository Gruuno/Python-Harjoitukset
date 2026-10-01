# Project α

## Pelin idea

Project α ideana on olla tekstipohjainen seikkailupeli, jossa pelaaja joutuu tutkimaan vanhaa hylättyä taloa, kun ovi paiskahti kiinni takaa heti astuttuaan sisään. Pelaajan tehtävänä on liikkua talon eri huoneissa, tutkia ympäristöä ja kerätä vastaan tulevia esineitä.

Pelin tarkoituksena on myöhemmin rakentaa pieni pulmapeli, jossa kaikkia esineitä ei kerätä vain varastoon, vaan niitä tarvitaan myös etenemiseen. Esimerkiksi pelaaja voi löytää avaimen, jolla saa avattua lukitun komeron. Komerosta voi löytyä taskulamppu, jota tarvitaan pimeässä kellarissa liikkumiseen. Joka sitten kenties avaa mahdollisuuden pelaajalle päästä ulos talosta.

## Toimintaperiaate

Ohjelman käynnistyessä kysytään nimi, jonka jälkeen pelaaja sijoitetaan pelin ensimmäiseen huoneeseen (eteinen/entryway). Pelaaja voi valita valikosta eri toimintoja:

- liikkua huoneesta toiseen
- kerätä huoneessa olevan esineen
- tarkastella mukana olevia esineitä
- tarkastella nykyistä sijaintia ja huoneen kuvausta
- lopettaa pelin

Pelaaja, huoneet ja esineet ovat omia luokkiaan, joiden avulla pelin eri osat voidaan pitää erillään ja niitä voidaan kehittää itsenäisesti.

## Projektin rakenne

'pelaaja' kansio sisältää 'Pelaaja'-luokan. Pelaajalla on nimi, sijainti sekä lista kerätyistä esineistä.

'huone' kansio sisältää 'Huone'-luokan. Huoneella on nimi, kuvaus ja mahdollinen esine.

'esine' kansio sisältää 'Esine'-luokan. Esineellä on nimi ja paino.

'main.py' sisältää ohjelman käynnistyksen sekä pelin päävalikon.

## Kestävä kehitys

Koodi on jaettu pieniin ja selkeästi määriteltyihin luokkiin ja tiedostoihin, mikä tekee ohjelmasta helpommin ylläpidettävän ja laajennettavan. Näin samoja rakenteita voidaan hyödyntää myöhemmin ilman, että koko ohjelmaa tarvitsee tehdä uudelleen.
Tämä periaatteessa kestävää kehitystä(?)

Vaikka tarina ei ehkä ole tärkein osio, voi myöskin alustavasti selvittää jossain, että pelaaja osti vanhan hylätyn talon halvalla, kestävä kehitys mielessään. Mutta jäi nalkkiin taloon, kun astui sisään etuovesta. 

[jos totta puhutaan, unohdin kokonaan tuon kestävän kehityksen osion, joten joudun varmaa muuttamaan/kääntämään aika monta osaa ennen 9.10.]