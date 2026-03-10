import dictionary as d
import richWord as rw


class MultiDictionary:

    def __init__(self):
       self.dictionaries = {}

    def addDictionary(self,language,dictionary):
        self.dictionaries[language]=dictionary

    def printDic(self, language):
        if language in self.dictionaries:
            self.dictionaries[language].printAll()
        else:
            print("Lingua non trovata")


    def searchWord(self, words, language):
        risultato = []
        # Accediamo al dizionario specifico salvato in self.dictionaries
        dictionary_obj = self.dictionaries[language].dict

        for w in words:
            rich = rw.RichWord(w)
            if w in dictionary_obj:
                rich.corretta = True
            else:
                rich.corretta = False
            risultato.append(rich)
        return risultato




