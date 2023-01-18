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


class Student(Person):
    def __init__(self,name,last,birth,lectures):
        super().__init__(name,last,birth)
        self._lectures = lectures

    def getLectures(self):
        return self._lectures

    def setLectures(self,lectures):
        self._lectures = lectures

    def _calculate_avg(self):
        acc = 0

        for (_,mark) in self._lectures.items(): 
            acc += mark
        
        return acc/len(self._lectures)

    grade_average = property(_calculate_avg, None, None, None)

    def __repr__(self):
        return self.__class__.__name__ + ": " + self._name + " " + self._last + ", born in " + str(self._birth)  \
                + ", grades: " + str(self._lectures) + " (avg: " + str(self.grade_average) + ")"


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


class Wizard(Person):
    
    def _get_age(self):
        today = date.today()
        return today.year - self._birth.year - ((today.month, today.day) < (self._birth.month, self._birth.day))

    def _set_age(self,age):
        self._birth = self._birth.replace(year = (date.today().year - age))  
        print("{} is now {} yo".format(self.getName(),self.age))

    age = property(_get_age, _set_age, None, None)

    def __repr__(self):
        return self.__class__.__name__ + ": " + self._name + " " + self._last + ", born in " + str(self._birth) + "({} yo)".format(self.age)


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
