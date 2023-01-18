from datetime import date
from types import FunctionType

class Multi(type):
    def __new__(cls, classname, supers, classdict):
        for attr, val in classdict.items():
            if type(val) is FunctionType and not attr.startswith('__'):
                classdict[attr] = decor(attr,val)
        return type.__new__(cls,classname,supers,classdict)        

def decor(name,func):
    def wrapper(*args):

        if name in wrapper.calls_map and wrapper.calls_map[name]:
            wrapper.calls_map[name]=False
            print('Calling ',name)
            return func(*args)
        else:
            wrapper.calls_map[name]=True
            print(name,' must be called twice')
            pass

    wrapper.calls_map = dict()        
    return wrapper       

class Person(metaclass=Multi):
    def __init__(self,name,last,birth):
        self._name = name
        self._last = last
        self._birth = birth

    def getName(self):
        return self._name

    def getLast(self):
        return self._last

    def getBirth(self):
        return self._birth

    def setName(self,name):
        self._name = name

    def setLast(self,last):
        self._last = last

    def setBirth(self,birth):
        self._birth = birth

    def __repr__(self):
        return self.__class__.__name__ + ": " + self._name + " " + self._last + ", born in " + str(self._birth)


if __name__ == "__main__":

    p = Person('Paola','Banana',date(2010,2,2))
    print(p.getName(),p.getName())
