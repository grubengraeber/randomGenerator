import random

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

def familieFunc():
        print (random.choice(familie))

def nummerFunc():
        print (random.choice(nummer))

def sportFunc():
        print (random.choice(sport))

def farbeFunc():
        print (random.choice(farbe))

def songFunc():
        print (random.choice(song))

def essenFunc():
        print (random.choice(essen))

def filmFunc():
        print (random.choice(film))

def hobbyFunc():
        print (random.choice(hobby))

def eigenschaftFunc():
        print (random.choice(eigenschaft))

def gegenstandFunc():
        print (random.choice(gegenstand))

def spracheFunc():
        print (random.choice(sprache))
    
#print("Gib für folgendes, folgendes ein: familie -> familieFunc(), nummer -> nummerFunc(), sport -> sportFunc(), farbe -> farbeFunc(), song -> songFunc(), essen -> essenFunc(), film -> filmFunc(), hobby -> hobbyFunc(), eigenschaft -> eigenschaftFunc(), gegenstand -> gegenstandFunc(), sprache -> spracheFunc();    Viel Spaß :)")
# while True:
print("sprache: ") 
spracheFunc() 
print("gegenstand: ") 
gegenstandFunc() 
print("eigenschaft: ") 
eigenschaftFunc()
print("hobby: ") 
hobbyFunc()
print("film: ") 
filmFunc()
print("essen: ") 
essenFunc()
print("song: ") 
songFunc()
print("farbe: ") 
farbeFunc()
print("sport: ") 
sportFunc()
print("nummer: ") 
nummerFunc()
print("familie: ") 
familieFunc()
#     print(familie[randint(0,len(familie)-1)]+" "+essen[randint(0,len(essen)-1)]+" "+film[randint(0,len(film)-1)]) 
#     print(len(familie))
#     break
