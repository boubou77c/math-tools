# math-tools

The math-tool.py Python module provides functions to perform various mathematical calculations.
Gestion des erreurs

Error Management 

The module defines several exceptions for error handling:

NotEquation: Exception thrown when an equation is invalid.
RootError: Exception thrown when a root of a negative number is attempted.
FactorialError: Exception thrown when a factorial calculation for a negative number is attempted.


How to use it ? 

Equation First degree:

(format : a + x = b / 4 + 2x = 8)

print(Equation(4,2,8).eq1())

Equation 2nd degree :

(format : 2x^2 +5x -3 = 0 / 2x^2 + 5x -3 = 0)

print(Equation(2,5,-3).eq2())



Geometry :

Geometry tool , you call Geometry(arg1,arg2,radius) + action

print(Geometry(radius=12).area_crcle())
print(Geometry(3,4).area_rctgl())


MathCalculate :

MathCalculate(arg1) + action

ex : print(MathCalculate(45).prime_factors())


Fraction :

Fraction(numerator,denominator) + action

(gcd = Greatest common divisor / lcm = Least common multiple)

ex : print(Fraction(32,21).gcd())

!!! if you do irr() you can choose the result :

-'m' = result decimal and normal (ex : (1/2, 0.5)

-'d' = result decimal (ex : 0.5)

-empty = standard result (1/2)


Statistic :

Statistic(*args) + action


ex : print(Statistic(12,12,12,23,5,2,1).median())


I will improve it over time, if you have any suggestion tell me on discord : _bou_bou_

Thank you




