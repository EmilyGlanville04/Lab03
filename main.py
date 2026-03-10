import spellchecker
import dictionary as d
import multiDictionary as md

ita = d.Dictionary("italiano")
ita.loadDictionary("resources/Italian.txt")

eng = d.Dictionary("inglese")
eng.loadDictionary("resources/English.txt")

spa = d.Dictionary("spagnolo")
spa.loadDictionary("resources/Spanish.txt")
# creazione MultiDictionary
multi = md.MultiDictionary()
multi.addDictionary("italian", ita)
multi.addDictionary("english", eng)
multi.addDictionary("spanish", spa)

sc = spellchecker.SpellChecker(multi)
#sc = spellchecker.SpellChecker()

while(True):
    sc.printMenu()

    txtIn = input()
    # Add input control here!

    if txtIn.isdigit() and int(txtIn)<5:
        if int(txtIn) == 1:
            print("Inserisci la tua frase in Italiano\n")
            txtIn = input()
            sc.handleSentence(txtIn,"italian")
            continue

        if int(txtIn) == 2:
            print("Inserisci la tua frase in Inglese\n")
            txtIn = input()
            sc.handleSentence(txtIn,"english")
            continue

        if int(txtIn) == 3:
            print("Inserisci la tua frase in Spagnolo\n")
            txtIn = input()
            sc.handleSentence(txtIn,"spanish")
            continue

        if int(txtIn) == 4:
            break
    else:
        raise ValueError("Valore non valido")

