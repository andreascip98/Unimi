from datetime import date

class Counter(type):
    cont = 0
    def __call__(cls, *args):
        Counter.cont += 1
        print(cls.__name__,'was instantiated {} times...'.format(Counter.cont))
        return type.__call__(cls, *args)


class Person(metaclass=Counter):
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

    p = Person('Paolo','Bane',date(2000,2,2))
    p = Person('Paola','Banana',date(2010,2,2))
    print(p)
