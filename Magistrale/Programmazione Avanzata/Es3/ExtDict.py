class ExtDict(dict):
    def __init__(self,**items):
        super().__init__({x:y for x,y in sorted(items.items())})
        print(self)

    def add(self,**items):
        super().__init__({x:y for x,y in sorted({**self,**items}.items())})
        print(self)
