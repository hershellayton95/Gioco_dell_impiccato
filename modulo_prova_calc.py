class Calc:
    
    def __init__(self):
        self.result = 0
        self.operazione = "+"
        
    def setOperando1(self, n):
        self.op1 = n
    
    def setOperando2 (self,n):
        self.op2 = n
    
    def setOperazione (self, op):
        self.operazione = op
        
    def getResult(self):
        self.calcola()
        return self.result
    
    def __str__(self):
        return f"{self.op1} {self.operazione} {self.op2} = {self.result}"
    
    def calcola(self):
        if self.operazione == "+":
            self.result = self.op1 + self.op2;
        elif self.operazione == "-":
            self.result = self.op1 - self.op2;
        elif self.operazione == "x":
            self.result = self.op1 * self.op2;
        elif self.operazione == "/":
            if not self.op2 == 0:
                self.result = self.op1 / self.op2
            else:
                self.result = "non si può dividere per 0"
        elif self.operazione == "pow":
            self.result = self.op1**self.op2;
        
        elif self.operazione == "rn":
            if not self.op2 == 0:
                self.result = self.op1**(1/self.op2);
            else:
                self.result = "non si può fare la radice di 0"
        else:
            self.result ="operazione non trovata"
           
    
if __name__ == "__main__":
    print ("script non eseguibile")