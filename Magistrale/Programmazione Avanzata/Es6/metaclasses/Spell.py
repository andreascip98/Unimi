from datetime import date

class Person():
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

class Worker(Person):
    def __init__(self,name,last,birth,pph):
        super().__init__(name,last,birth)
        self._pph = pph

    def getPph(self):
        return self._pph

    def setPph(self,pph):
        self._pph = pph

    def _get_salary(mul):
        def compute(self):
            return self._pph*mul
        return compute

    def _set_salary(div):
        def compute(self,amount):
            tmp = amount/div
            print("{}'s pph changed to: {:.2f}".format(self.getName(),tmp))
            self._pph = tmp
        return compute

    day_salary = property(_get_salary(8), _set_salary(8), None, None)
    week_salary = property(_get_salary(8*5), _set_salary(8*5), None, None)
    month_salary = property(_get_salary(8*5*4), _set_salary(8*5*4), None, None)
    year_salary = property(_get_salary(8*5*4*12), _set_salary(8*5*4*12), None, None)

    def __repr__(self):
        return self.__class__.__name__ + ": " + self._name + " " + self._last + ", born in " + str(self._birth)  \
                + ", pph: {:.2f}, ppd: {:.2f}, ppw: {:.2f}, ppm: {:.2f}, ppy: {:.2f}".format( \
                self._pph, self.day_salary, self.week_salary, self.month_salary, self.year_salary)

class Spell(type):
    def __new__(cls, *args):
        
        def init(self,name,lastname,birth):
            self._name = name
            self._last = lastname
            self._birth = birth
            self._pph = 10

        new_dict = Worker.__dict__.copy()
        new_dict['__init__'] = init
        return type.__new__(cls, Worker.__name__, Worker.__bases__, new_dict) 


class Person2(metaclass=Spell):
    def __init__(*args):
        Person.__init__(*args)


#..........................................MAIN.......................................................
if __name__ == "__main__":

    w = Person2('Lollo','Pallo',date(2003,4,4))
    print(w.getPph())
