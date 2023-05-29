from Exceptions import *

class strlist(object):
    class element:
        def __init__(self, char):
            self.char = char
            self.ptr = None

    def __init__(self, string):
        if not isinstance(string, str):
            raise BadInitValue("Error value")

        self.count = len(string)
        self.lst = self.element(string[0])
        p = self.lst
        for i in range(1, self.count):
            self.lst = self.addelement(string[i], "lst")

        self.end = self.lst
        self.lst = p

    def addelement(self, a, t):
        if t == "lst":
            p = self.lst.ptr
            temp = self.element(a)
            temp.ptr = p
            self.lst.ptr = temp
        else:
            p = self.end.ptr
            temp = self.element(a)
            temp.ptr = p
            self.end.ptr = temp

        return temp

    def del_el(self):
        if self.count == 0:
            raise BadCountException("Elements are too small!")
        if self.count == 1:
            self.count = 0
            self.lst = None
            return
        p = self.lst
        p1 = None
        while self.lst.ptr != None:
            p1 = self.lst
            self.lst = self.lst.ptr
        p1.ptr = None
        self.end = self.lst
        self.lst = p
        self.count -= 1

    def print(self):
        p = self.lst
        if self.count == 0:
            print("Empty")
            return
        while p != None:
            print(p.char, end=" ")
            p = p.ptr
        print()

    def __add__(self, other):
        if self.count + 1 > 1000:
            raise BadCountException("A lot of count!!!")
        if self.count == 0:
            self.lst = self.element(other)
            self.end = self.lst
            self.count = 1
            return self
        else:
            self.end = self.addelement(other, "end")
            self.count += 1
            return self

    def __radd__(self, other):
        if self.count + 1 > 1000:
            raise BadCountException("A lot of count!!!")
        if self.count == 0:
            self.lst = self.element(other)
            self.end = self.lst
            self.count = 1
            return self
        else:
            self.end = self.addelement(other, "end")
            self.count += 1
            return self

    def __ne__(self, other):
        if type(other) != type(self):
            raise BadEqualeException("Dont correct type")

        if self.lst == None or other.lst == None:
            raise BadCountException("Dont correct count!!!")

        if other.count == 0 and self.count == 0:
            return False
        if other.count != self.count:
            return True

        p1 = other.lst
        p2 = self.lst

        while other.lst != None and self.lst != None:
            if other.lst.char != self.lst.char:
                return True
            other.lst = other.lst.ptr
            self.lst = self.lst.ptr
        other.lst = p1
        self.lst = p2
        return False
