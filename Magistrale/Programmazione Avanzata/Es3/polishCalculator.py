import re as r

class PolishCalculator:
    
    def __init__(self): self._stack = []
    
    def printS(self): 
        print("\n##########")
        for x in self._stack: print("# "+x+" #");
        print("##########")

    def __str__(self): pass

    def evaluate(self,s):
        for token in s.split():
\
            #OPERANDS
            if r.search("\d+(?:\.\d+)?|[TF]",token): 
                if token=="T": self._stack.append("True")
                elif token=="F": self._stack.append("False")
                else: self._stack.append(token) 
                self.printS()

            #UNARY OPERATORS
            elif r.search("not",token): 
                print("\nOperator: ",token)
                self._stack.append(str(eval(token +" "+ self._stack.pop())))
                self.printS()

            #BINARY OPERATORS
            elif r.search("\*{2}|[+\-*/]|or|and",token): #\*{2} is to catch **  
                print("\nOperator: "+token)
                operand2 = self._stack.pop()
                operand1 = self._stack.pop()
                self._stack.append(str(eval(operand1 +" "+ token +" "+ operand2)))
                self.printS()
        
        print("\nResult: "+self._stack.pop()+"\n")

if __name__ == "__main__":

    c = PolishCalculator()
    c.evaluate("3 4 + 5 6.3 ** *") # (3+4)*(5+6)
    c.evaluate("F F or")
    c.evaluate("T not F not and")
    c.evaluate("4 -")
    c.evaluate("4 - 5")
    #print(c)


