from random import randint

class Dictionary():
    def __init__(self):
        self.count = 0
        with open("L014-words.txt", 'r') as f:
            for line in f:
                self.count += 1


            
    def randword(self, minlen):
        word = ""
        lw = 0
        while lw < minlen:
            rn = randint(0,self.count-1)
            with open("L014-words.txt", 'r') as f:
                for i, line in enumerate(f):
                    if i == rn:
                        word = line.strip().upper()
                        break
            lw = len(word)
        return word

class Hangman():
    
    MINLEN = 6
    
    def __init__(self):
        self.dict = Dictionary()
        self.tentativi = self.getTent()
        self.letters = []
        
    def getTent(self):
        tent = 6
        lev = "0"
        while lev == "0":
            lev = input(f"che livello scegli? (1, 2 o 3) ")
            if lev == "1":
                tent = 6
            elif lev == "2":
                tent = 4
            elif lev == "3":
                tent = 3
            else:
                print ("scelta non valida")
                lev = "0"
        return tent
                
        
    
    def play(self):
        self.secret = self.dict.randword(self.MINLEN).upper()
        #print(self.secret)
        n = len(self.secret)
        print("Parola con", n, "lettere")
        
        while True:
            print("Hai", self.tentativi, "tentativi")
            if self.tentativi == 0:
                print(f"Fine gioco. La parola era {self.secret}")
                break
            
            w, c = self.masked()
            print(w)
            print("")
            if c == n:
                print("Gioco Finito")
                break
            ch = input("che lettera? ").upper()

            if ch in self.secret and not ch in self.letters:
                self.letters.append(ch)
                print(ch, "è presente")
                print("")
            elif ch in self.letters:
                print("Già scritto")
                print("")
            else:
                print("Non presente")
                self.tentativi -= 1
        
    def masked(self):
        #ogni volta che chiamo masked c = 0 e se trovo n corrispondenze
        #in letter allora c = n corrispondenze
        s = ""
        c = 0 
        for ch in self.secret:
            if not ch in self.letters:
                s += "_ "
            else:
                s += ch+" "
                c += 1
        return s, c
        
p = Hangman()
p.play()
