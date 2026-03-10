class Dictionary:
    def __init__(self, language: str):
        self.language = language
        self._parole=[]

    def loadDictionary(self,path):
        with open(path, "r", encoding="UTF-8") as file:
            for riga in file:
                parola = riga.strip().lower()
                self._parole.append(parola)


    def printAll(self):
        for parola in self._parole:
            print(parola)


    @property
    def dict(self):
        return self._parole
