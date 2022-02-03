import random
from tkinter.tix import InputOnly

#familie
eins = ["Frau", "Mama", "Vater", "Opa", "Oma", "Cousin", "Cousine", "Schwester", "Bruder", "Halbschwester", "Halbbruder"]
#nummer
zwei = ["eins", "zwei", "drei", "vier", "fünf", "sechs", "sieben", "acht", "neun", "zehn"]
#sport
drei = ["laufen", "tanzen", "klettern", "tennis", "fußball", "kunstturnen", "skaten", "basketball"]
#farbe
vier = ["grün", "blau", "schwarz", "weiß", "gelb", "organge", "braun", "grau", "türkis", "cyan"]
#song
fuenf = ["purple noise  - Boris Brejcha", "wer hat die Kokosnuss geklaut - Sternschnuppe", "could you be loved - Bob Marley", "Under and over it - five finger death punch", "summer sun - Cari Cari", "TARAKA - Gordo", "I'm living - sizzla", "great plains - klangphonics", "Young black intelligent - Masta Ace", "Nikes - Frank Ocean"]
#essen
sechs = ["Pizza", "Pasta", "Gulasch", "Auflauf", "Kaiserschmarrn", "Strudel", "Suppe", "Eierreis", "Salat", "Ofenkartoffel"] 
#film
sieben = ["Batman Trilogie", "Marvel movies", "Fast and the furious", "Fluch der Karibik", "Harry Potter", "John Wick", "Kung Fu Panda", "James Bond", "Kingsman", "Interstellar"] 
#hobby
acht = ["löten", "schweißen", "drechseln", "sprachen", "reisen", "kino", "fortgehen", "essen gehen", "schießen gehen", "neues ausprobieren"] 
#eigenschaft
neun = ["freundlich", "grantig", "hilfsbereit", "müde", "energetisch", "gelangweilt", "empört", "erschrocken", "neugierig", "wütend"]
#gegenstand
zehn = ["Hut", "Kopfhörer", "Handy", "Computer", "Stift", "Bett", "Auto", "Taschenlampe", "Ruderboot", "Papier"] 
#sprache
elf = ["deutsch", "englisch", "spanisch", "russisch", "französisch", "chinesisch", "japanisch", "yoruba", "farsi", "hebräisch"]

# def familieFunc():
#         print (random.choice(familie))

# def nummerFunc():
#         print (random.choice(nummer))

# def sportFunc():
#         print (random.choice(sport))

# def farbeFunc():
#         print (random.choice(farbe))

# def songFunc():
#         print (random.choice(song))

# def essenFunc():
#         print (random.choice(essen))

# def filmFunc():
#         print (random.choice(film))

# def hobbyFunc():
#         print (random.choice(hobby))

# def eigenschaftFunc():
#         print (random.choice(eigenschaft))

# def gegenstandFunc():
#         print (random.choice(gegenstand))

# def spracheFunc():
#         print (random.choice(sprache))
    
#print("Gib für folgendes, folgendes ein: familie -> familieFunc(), nummer -> nummerFunc(), sport -> sportFunc(), farbe -> farbeFunc(), song -> songFunc(), essen -> essenFunc(), film -> filmFunc(), hobby -> hobbyFunc(), eigenschaft -> eigenschaftFunc(), gegenstand -> gegenstandFunc(), sprache -> spracheFunc();    Viel Spaß :)")
# while True:
# print("sprache: ") 
# spracheFunc() 
# print("gegenstand: ") 
# gegenstandFunc() 
# print("eigenschaft: ") 
# eigenschaftFunc()
# print("hobby: ") 
# hobbyFunc()
# print("film: ") 
# filmFunc()
# print("essen: ") 
# essenFunc()
# print("song: ") 
# songFunc()
# print("farbe: ") 
# farbeFunc()
# print("sport: ") 
# sportFunc()
# print("nummer: ") 
# nummerFunc()
# print("familie: ") 
# familieFunc()
#     print(familie[randint(0,len(familie)-1)]+" "+essen[randint(0,len(essen)-1)]+" "+film[randint(0,len(film)-1)]) 
#     print(len(familie))
#     break

# INPUT FROM USER IMPLEMENTATION TO CHOOSE A SPECIFIC CATEGORY TO GET
inputQuestion = '''
Do only pick one for now. \n
What do you want to choose from. \n 
Pick 1 for: a family member \n 
Pick 2 for: a number \n 
Pick 3 for: a sport \n 
Pick 4 for: a color \n 
Pick 5 for: a song \n 
Pick 6 for: a food \n 
Pick 7 for: a movie \n 
Pick 8 for: a hobby \n 
Pick 9 for: a characteristic \n 
Pick 10 for: a thing \n 
Pick 11 for: a language 
Insert number betweeen 1 and 11 here:'''


while True:
        morningAttendance = input(inputQuestion)

        if morningAttendance.isnumeric == False and morningAttendance < 1 and morningAttendance > 11:
                print("Type in a number between 1 and 11 including both of these")
                continue

        elif morningAttendance == "1":
                print(random.choice(eins))
                break

        elif morningAttendance == "2":
                print(random.choice(zwei))
                break
                
        elif morningAttendance == "3":
                print(random.choice(drei))
                break

        elif morningAttendance == "4":
                print(random.choice(vier))
                break

        elif morningAttendance == "5":
                print(random.choice(fuenf))
                break

        elif morningAttendance == "6":
                print(random.choice(sechs))
                break

        elif morningAttendance == "7":
                print(random.choice(sieben))
                break

        elif morningAttendance == "8":
                print(random.choice(acht))
                break

        elif morningAttendance == "9":
                print(random.choice(neun))
                break

        elif morningAttendance == "10":
                print(random.choice(zehn))
                break

        elif morningAttendance == "11":
                print(random.choice(elf))
                break