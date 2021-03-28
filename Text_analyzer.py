TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''', '''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''', '''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.''']

users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
oddelovac = "-" * 40

username = input("username:")
password = input("password:")
print(oddelovac)

if username in users and password in list(users.values()):
    print("Welcome to app,", username)
    print("We have 3 texts to be analyzed.")
    print(oddelovac)
else:
    print("Invalid username or password, terminating")
    print(oddelovac)
    quit()

volba = int(input("Enter a number btw. 1 and 3 to select: "))
print(oddelovac)

if not 0 < volba <= len(TEXTS):
    print("Choice not availabe, terminating")
    quit()
# prevede zvoleny text na list
textlist = TEXTS[volba-1].split()

titlecase = []
uppercase = []
lowercase = []
numeric = []
for i in textlist:
    if i[0].isupper():
        titlecase.append(i)
    elif i.isupper():
        uppercase.append(i)
    elif i.islower():
        lowercase.append(i)
    elif i.isnumeric:
        numeric.append(int(i))
print("There are", len(textlist), "words in selected text.")
print("There are", len(titlecase), "titlecase words.")
print("There are", len(uppercase), "uppercase words.")
print("There are", len(lowercase), "lowercase words.")
print("The sum of all the numbers", sum(numeric))

# ocisti jednotliva v listu textlist od znaku ,.
ocistit = []
for slovo in textlist:
    x = slovo.strip(".,")
    ocistit.append(x)

# vytvori list delek jednotlivych slov
delkaslov = []
for i in ocistit:
    delkaslov.append(len(i))

# vytovri set jednotlivych delek
delky = set(delkaslov)

# zjisti, kterych slov je nejvice. Nize pouzito pro formatovani textu v grafu
nejvice = []
for i in delky:
    nejvice.append(delkaslov.count(i))

# vytvori graf a formatuje jej podle cetnosti jednotlivych delek slov - mozna trosku slozita hloupost,
# ale udelala mi radost :)
print(oddelovac)
if max(nejvice) < 10:
    print("LEN| OCCURANCES |NR.")
    print(oddelovac)
    for i in delky:
        print(str(i).rjust(3) + "|" + delkaslov.count(i) * "*" + " " * (12 - delkaslov.count(i)) + "|",
              delkaslov.count(i))
else:
    print("LEN|" + "OCCURANCES".center(max(nejvice) + 2) + "|NR.")
    print(oddelovac)
    for i in delky:
        print(str(i).rjust(3) + "|" + delkaslov.count(i) * "*" + " " * (max(nejvice) + 2 - delkaslov.count(i)) + "|",
              delkaslov.count(i))
