import itertools

class monoid:
    def __init__(self, S, add, i):
        self._set = S
        self._oper = add
        self._ident = i

    def check(self):
        first = self._ident
        for elem in self._set:
            print("add({0},{1}): {2}".format(first,elem,self._oper(first,elem)))
            first = elem

class group: 
    def __init__(self, S, add, i):
        self._set = S
        self._oper = add
        self._ident = i

    def check(self):
        first = self._ident
        for elem in self._set:
            print("add({0},{1}): {2}".format(first,elem,self._oper(first,elem)))
            first = elem

class ring:
    def __init__(self, S, add, mul, i):
        self._set = S
        self._add = add
        self._mul = mul
        self._ident = i

    def check(self):
        first = self._ident
        for elem in self._set:
            print("add({0},{1}): {2}\nmul({0},{1}): {3}".format(first,elem,self._add(first,elem),self._mul(first,elem)))
            first = elem

if __name__ == "__main__":
    

    #a = lambda x,y,z: (y,x,z)
    #b = lambda x,y,z: (x,z,y)

    items = [ \
    monoid({False,True}, lambda x,y: x or y, False), \
    monoid({x for x in range(1,6)}, lambda x,y: (x+y)%7, 0), \
    #group(itertools.permutations('RGB'), lambda x: a(*b(*x)) , lambda x: a(*a(*x))), \
    group({(x+1)/x for x in range (1,10)}, lambda x,y: x*y, 1), \
    ring({0}, lambda x,y: x+x, lambda x,y: x*y, 0), \
    ring({0,1,2,3}, lambda x,y: (x+y)%4, lambda x,y: (x*y)%4, 0)
    ]    

    for item in items: print(""); item.check()


