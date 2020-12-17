"""
Assignment 1 question4 Fraction OOP solutions
"""

class Fraction:
    def __init__(self, numerator = 0, denominator = 1):
        self.numerator = numerator
        if denominator != 0:
            self.denominator = denominator
        else:
            raise ZeroDivisionError()

    def __add__(self, other):
        '''
        @other: a class Fraction object, the other fraction number.
        DO NOT MODIFY self.
        @return: a ***new*** class Fraction object, which is the sum of self + other.
        '''
        result = Fraction()
        result.denominator = self.denominator * other.denominator
        result.numerator = self.numerator * other.denominator + self.denominator * other.numerator
        return result

    def __iadd__(self, other):
        '''
        @other: a class Fraction object, the other fraction number.
        @return: self. The value of self should become the sum of self + other.
        '''
        self.denominator = self.denominator * other.denominator
        self.numerator = self.numerator * other.denominator + self.denominator * other.numerator
        return self

    def __sub__(self, other):
        '''
        @other: a class Fraction object, the other fraction number.
        @return: a new class Fraction object, which is the subtraction of self - other.
        '''
        result = Fraction()
        result.denominator = self.denominator * other.denominator
        result.numerator = self.numerator * other.denominator - self.denominator * other.numerator
        return result

    def __mul__(self, other):
        '''
        @other: a class Fraction object, the other fraction number.
        @return: a new class Fraction object, which is the multiplication of self * other.
        '''
        result = Fraction()
        result.denominator = self.denominator * other.denominator
        result.numerator = self.numerator * other.numerator
        return result

    def __eq__(self, other):
        '''
        @other: a class Fraction object, the other fraction number.

        If you use the reduce function here, it is fine.

        @return: True if the float value of self is equal to other;
                 False if the float value of self is not equal to other.
        '''
        self.reduce()
        other.reduce()
        return self.denominator == other.denominator and self.numerator == other.numerator

    def reduce(self):
        '''
        Reduces the self Fraction object. 
        Modifies self.numerator and self.denominator.
        For example: 12 / 24 --> 1 / 2;  16 / 20 --> 4 / 5

        @return: Nothing.
        '''
        gcd = GCD(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

    def __str__(self):
        '''
        Displays the self Fraction object nicely. 
        Recommended format:
        Suppose,
        self.numerator = 5
        self.denominator = 6
        Then, should return "5 / 6"

        @return: The string representation of self Fraction object.
        '''
        return str(self.numerator) + " / " + str(self.denominator)

def GCD(a, b):
    while (b != 0):
        temp = a % b
        a = b
        b = temp
    return a




