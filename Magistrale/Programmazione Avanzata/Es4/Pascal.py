class Pascal:
    def __init__(self,m):
        self.max = m

    def __iter__(self):
        self.col=0
        self.row=0
        self.vals = [1]
        return self
    
    def __next__(self):
        
        curPos = len(self.vals)
        
        if (curPos > self.max): raise StopIteration
        
        if (self.col == 0 and self.row == 0): curPos -= 1

        else:    
            prevVal = 0 if self.col == 0 else self.vals[curPos-self.row-1]
            nextVal = 0 if self.col == self.row else self.vals[curPos-self.row]
            self.vals.append(prevVal + nextVal)
        
        if (self.col >= self.row):
            self.col = 0
            self.row += 1

        else: self.col +=1
        
        return self.vals[curPos]
        
if __name__ == "__main__":
   
    p = Pascal(10)
    for e in Pascal(10): print(e)
