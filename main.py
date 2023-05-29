from strlist import *
import copy

print("Program 1: ")
try:
    b = strlist("asd")
    b.print()

    # don't correct
    a = strlist(123)

except BadInitValue as e:
    print(e.message)

print()
print("Program 2: ")
try:
    a = strlist("qqq")
    a = a + "1"
    a.print()
    a = "2" + a
    a.print()
    print("-----")

    # don't correct
    for i in range(10000):
        a = a + 'k'

    a.print()
except BadCountException as e:
    print(e.message)

print()
print("Program 3: ")
try:
    c1 = strlist("123")
    c2 = strlist("123")
    c3 = strlist("111")

    print(c1 != c2)
    print(c1 != c3)

    # don't correct
    print(c1 != 1)

except BadEqualeException as e:
    print(e.message)

print()
print("Program 4: ")
try:
    d = strlist("1234")

    d.del_el()
    d.del_el()

    d.print()

    d.del_el()
    d.del_el()

    # don't correct
    d.del_el()

except BadCountException as e:
    print(e.message)
