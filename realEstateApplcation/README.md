Имате задача да креирате систем за управување со агенција за недвижности. Системот треба интуитивно да ги прикажува недвижностите кои се продаваат, да нуди информации за агентите кои се задолжени за продажба и да овозможува лесно пребарување на недвижностите според карактеристиките кои ги имаат. Секоја недвижност која може да се огласи за продавање се карактеризира со име, опис на локацијата каде се наоѓа, површина која ја зафаќа, датум кога е објавена за продавање, фотографија, информација дали некој ја резервирал и информација дали е веќе можеби продадена. Агентите кои се задолжени за продажба во агенцијата се карактеризираат со име и презиме, телефон за контакт, линк до нивен профил од LinkedIn, број на извршени продажби до сега и email адреса. Еден агент може да биде одговорен за повеќе недвижности, а една недвижност може да ја нудат повеќе агенти. Агентите задолжени за одредена недвижност лесно се додаваат во Админ панелот во делот за недвижност. Недвижноста нема почетна цена, туку таа се креира како сума од вредностите на карактеристиките кои таа недвижност ги поседува. На пример, доколку недвижнота располага со лифт, тогаш во цената се додава $10000, поседувањето на базен е $25000 итн (цените ги одредувате Вие при креирање на карактеристиките). Карактеристиките за една недвижност исто така се додаваат во делот за недвижности.


Апликацијата ќе вклучува почетна страница и страница за менување/уредување на огласите за продажба. Исто така потребно е и одредено прилагодување во административниот панел на Django.


Притоа, во рамки на aдмин панелот потребно е да ги обезбедите следните функционалности


Агенти и Карактеристики може да бидат додадени само од супер-корисници
Агентите, Карактеристиките и Недвижностите се прикажани со нивното име (презиме, површина и опис ако ги имаат, соодветно)
Огласи за продажба може да бидат додадени само од агенти и по автоматизам агентот кој додава оглас е еден од задолжените за продажба на таа недвижност
Еден оглас може да биде избришан само ако нема додадено ниту една карактеристика која го опишува
Огласите можат да бидат менувани само од агенти кои се задолжени за продажба на тој оглас, а останатите агенги може само да ги гледаат тие огласи
На супер-корисниците во Админ панелот им се прикажуваат само огласите кои се објавени на денешен датум
Кога еден оглас/недвижнина ќе се означи како продадена, потребно е сите агенти поврзани со неа да ја инкрементираат својата продажба
Web апликацијата се состои од една почетна страна, прикажана на сликата подолу која ги прикажува сите недвижности кои не се продадени и нивната површина е поголема од 100 метри квадратни.