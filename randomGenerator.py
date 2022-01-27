from random import randint
from stat import filemode
familie=["Frau", "Mama", "Vater", "Opa", "Oma", "Cousin", "Cousine", "Schwester", "Bruder", "Halbschwester", "Halbbruder"]
nummer=["eins", "zwei", "drei", "vier", "fünf", "sechs", "sieben", "acht", "neun", "zehn"]
sport=["laufen", "tanzen", "klettern", "tennis", "fußball", "kunstturnen", "skaten", "basketball"]
farbe=["grün", "blau", "schwarz", "weiß", "gelb", "organge", "braun", "grau", "türkis", "cyan"]
song=["purple noise  - Boris Brejcha", "wer hat die Kokosnuss geklaut - Sternschnuppe", "could you be loved - Bob Marley", "Under and over it - five finger death punch", "summer sun - Cari Cari", "TARAKA - Gordo", "I'm living - sizzla", "great plains - klangphonics", "Young black intelligent - Masta Ace", "Nikes - Frank Ocean"]
essen=["Pizza", "Pasta", "Gulasch", "Auflauf", "Kaiserschmarrn", "Strudel", "Suppe", "Eierreis", "Salat", "Ofenkartoffel"] 
film=["Batman Trilogie", "Marvel movies", "Fast and the furious", "Fluch der Karibik", "Harry Potter", "John Wick", "Kung Fu Panda", "James Bond", "Kingsman", "Interstellar"] 
hobby=["löten", "schweißen", "drechseln", "sprachen", "reisen", "kino", "fortgehen", "essen gehen", "schießen gehen", "neues ausprobieren"] 
eigenschaft=["freundlich", "grantig", "hilfsbereit", "müde", "energetisch", "gelangweilt", "empört", "erschrocken", "neugierig", "wütend"]
gegenstand=["Hut", "Kopfhörer", "Handy", "Computer", "Stift", "Bett", "Auto", "Taschenlampe", "Ruderboot", "Papier"] 
sprache=["deutsch", "englisch", "spanisch", "russisch", "französisch", "chinesisch", "japanisch", "yoruba", "farsi", "hebräisch"]
while True:
    print(familie[randint(0,len(familie)-1)]+" "+essen[randint(0,len(essen)-1)]+" "+film[randint(0,len(film)-1)])
    break
