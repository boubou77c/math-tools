# ➗math-tools➗

math-tools can do various mathematical calculations


## 🚀 About Me
 I am a beginner programmer.

If you have any advice to improve my skills ,ideas to enhance my program or suggestions for creating new program, you can write me :

My discord : .bou_bou_


## 🛠Features🛠

- Geometry
- Fraction
- Statistic
- Equation
- root
- and more !


## Usage/Examples
- Equation First degree:

(format : a + x = b / 4 + 2x = 8)

- Equation 2nd degree :

(format : 2x^2 +5x -3 = 0 / 2x^2 + 5x -3 = 0)

Geometry tool , you call Geometry(arg1,arg2,radius) + action

- MathCalculate:

MathCalculate(arg1) + action


- Statistic:

Statistic(*args) + action

- Fraction:

Fraction(numerator,denominator) + action

(gcd = Greatest common divisor / lcm = Least common multiple)


!!! if you do irr() you can choose the result :

-'m' = result decimal and normal (ex : (1/2, 0.5)

-'d' = result decimal (ex : 0.5)

-empty = standard result (1/2)


```python
#Eq 1
print(Equation(4,2,8).eq1())

#Eq 2
print(Equation(2,5,-3).eq2())

#Geometry
print(Geometry(radius=12).area_crcle()) 
print(Geometry(3,4).area_rctgl())


#MathCalculate
print(MathCalculate(45).prime_factors())

#Statistic
print(Statistic(12,12,12,23,5,2,1).median())

#Fraction 
print(Fraction(32,21).gcd())
print(Fraction(23,12).irr("d"))

```
