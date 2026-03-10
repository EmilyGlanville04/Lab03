import time

import multiDictionary as md
import dictionary as d

class SpellChecker:


    def __init__(self,multi_dict):
            self._multi_dict = multi_dict




    def handleSentence(self, txtIn, language):
        start = time.time()
        clean_text = self.replaceChars(txtIn.lower())
        words = clean_text.split()
        results = self._multi_dict.searchWord(words, language)
        wrong = []
        for w in results:
            if not w.corretta:
                wrong.append(w)
        end_time = time.time()
        print("\nParole errate")
        for w in wrong:
            print(w.parola)
        print("\nNumero errori", len(wrong))
        print("Tempo di esecuzione", end_time-start, "secondi")



    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


    def replaceChars(self,text):
        chars = "\\'_{}[]()>#+-.!$%;,=-"
        for c in chars:
            text = text.replace(c, "")
        return text
