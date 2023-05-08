# Zadanie 1
class Element:
    def __init__(self, data=None, nextE=None):
        self.data = data
        self.nextE = nextE

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        res = []
        current = self.head
        while current is not None:
            res.append(str(current.data))
            current = current.nextE
        return ' -> '.join(res)

    def get(self, e):
        current = self.head
        while current is not None:
            if current.data == e:
                return current
            current = current.nextE
        return None

    def delete(self, e):
        prev = None
        current = self.head
        while current is not None:
            if current.data == e:
                if prev is None:
                    self.head = current.nextE
                else:
                    prev.nextE = current.nextE
                if current.nextE is None:
                    self.tail = prev
                self.size -= 1
                return True
            prev = current
            current = current.nextE
        return False

    def append(self, e, func=None):
        new_element = Element(e)
        if self.size == 0:
            self.head = new_element
            self.tail = new_element
            self.size += 1
            return
        if func is None:
            func = lambda x, y: x >= y
        prev = None
        current = self.head
        while current is not None:
            if func(current.data, e):
                new_element.nextE = current
                if prev is None:
                    self.head = new_element
                else:
                    prev.nextE = new_element
                self.size += 1
                return
            prev = current
            current = current.nextE
        self.tail.nextE = new_element
        self.tail = new_element
        self.size += 1


# Zadanie 2
class Student:
    def __init__(self, email, imie, nazwisko, punkty, ocena_projekt=None, oceny_list=None, oceny_domowe=None, ocena_koncowa=None, status=''):
        self.email = email
        self.imie = imie
        self.nazwisko = nazwisko
        self.punkty = float(punkty)
        self.ocena_projekt = ocena_projekt
        self.oceny_list = oceny_list or [-1, -1, -1]
        self.oceny_domowe = oceny_domowe or [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        self.ocena_koncowa = ocena_koncowa
        self.status = status

    def oblicz_srednia_domowe(self):
        oceny_domowe = [o for o in self.oceny_domowe if o >= 0]
        if len(oceny_domowe) > 0:
            return sum(oceny_domowe) / len(oceny_domowe)
        else:
            return None

    def oblicz_srednia(self):
        srednia_domowe = self.oblicz_srednia_domowe()
        if srednia_domowe is None:
            return None
        srednia_list = sum([o for o in self.oceny_list if o >= 0]) / len([o for o in self.oceny_list if o >= 0])
        srednia = 0.4 * self.ocena_projekt + 0.2 * srednia_list + 0.4 * srednia_domowe
        return srednia

class MySortedList(list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def sortuj(self):
        self.sort(key=lambda x: x.ocena_koncowa, reverse=True)


def wczytaj_studentow(filepath):
    students = {}
    with open(filepath) as file_object:
        for line in file_object:
            tymcz = line.split(",")
            email = tymcz[0]
            imie = tymcz[1]
            nazwisko = tymcz[2]
            ocena_projekt = int(tymcz[3])
            oceny_list = [int(tymcz[i]) for i in range(4, 7)]
            oceny_domowe = [int(tymcz[i]) for i in range(7, 17)]
            ocena_koncowa = tymcz[17] if tymcz[17] != '-1' else None
            status = tymcz[18].rstrip()
            student = Student(email, imie, nazwisko, 0, ocena_projekt, oceny_list, oceny_domowe, ocena_koncowa, status)
            students[email] = student
    return students
