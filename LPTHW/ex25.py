# - *- coding: utf- 8 - *-
class Parent(object):
    def override(self):
        print "PARENT override()"

    def implicit(self):
        print "PARENT implicit()"

    def altered(self):
        print "PARENT altered()"

class Child(object):
    def __init__(self):
        self.parent = Parent()

    def implicit(self):
        self.parent.implicit()

    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD before parent altered()"


dad = Parent()
son = Child()

dad.implicit()
son.implicit()
dad.override()
son.override()
dad.altered()
son.altered()
