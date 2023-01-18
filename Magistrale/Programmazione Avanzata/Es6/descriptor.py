from datetime import date

class Person:
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

#-------------------------------------------------------------------------------------------------------------------

class average_descriptor:
    def __get__(self, obj, _):
        acc = 0
        for (_,mark) in obj._lectures.items():
            acc += mark
        return acc/len(obj._lectures)

class Student(Person):
    def __init__(self,name,last,birth,lectures):
        super().__init__(name,last,birth)
        self._lectures = lectures

    def getLectures(self):
        return self._lectures

    def setLectures(self,lectures):
        self._lectures = lectures

    grade_average = average_descriptor()

    def __repr__(self):
        return self.__class__.__name__ + ": " + self._name + " " + self._last + ", born in " + str(self._birth)  \
                + ", grades: " + str(self._lectures) + " (avg: " + str(self.grade_average) + ")"

#-------------------------------------------------------------------------------------------------------------------

class salary_descriptor:
    def __init__(self, const):
        self._const = const

    def __get__(self, obj, _):
        return obj._pph*self._const

    def __set__(self,obj,amount):
        tmp = amount/self._const
        print(obj.getName(),"'s pph changed to: {:.2f}".format(tmp))
        obj._pph = tmp

class Worker(Person):
    def __init__(self,name,last,birth,pph):
        super().__init__(name,last,birth)
        self._pph = pph

    def getPph(self):
        return self._pph

    def setPph(self,pph):
        self._pph = pph

    day_salary = salary_descriptor(8)
    week_salary = salary_descriptor(8*5)
    month_salary = salary_descriptor(8*5*4)
    year_salary = salary_descriptor(8*5*4*12)

    def __repr__(self):
        return self.__class__.__name__ + ": " + self._name + " " + self._last + ", born in " + str(self._birth)  \
                + ", pph: {:.2f}, ppd: {:.2f}, ppw: {:.2f}, ppm: {:.2f}, ppy: {:.2f}".format( \
                self._pph, self.day_salary, self.week_salary, self.month_salary, self.year_salary)

#-------------------------------------------------------------------------------------------------------------------

class age_descriptor:
    def __get__(self, obj, _):
        today = date.today()
        return today.year - obj._birth.year - ((today.month, today.day) < (obj._birth.month, obj._birth.day))

    def __set__(self, obj, age):
        obj._birth = obj._birth.replace(year = (date.today().year - age))
        print(obj.getName(),'is now ',obj.age,'yo')

class Wizard(Person):
    
    age = age_descriptor()

    def __repr__(self):
        return self.__class__.__name__ + ": " + self._name + " " + self._last + ", born in " + str(self._birth) + "({} yo)".format(self.age)

#-------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":

    p = Person('Paolo','Bane',date(2000,2,2))
    print(p)

    s = Student('Lorenzo','Prop',date(1998,4,5),{'Storia':10,'Inglese':8.5})
    print(s)

    w = Worker('Gianluca','Stosi',date(1990,6,7),10)
    print(w)
    w.year_salary = 20000
    print(w)
    
    z = Wizard('Mago','Merletto',date(1860,1,7))
    print(z)
    z.age = 30
    print(z)
