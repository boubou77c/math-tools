#ERROR GESTION
class NotEquation(Exception):
    def __init__(self,message= 'It is not an Equation'):
        self.message= message

class RootError(Exception):
    def __init__(self,message="RootError: You can't calculate the Root of a negative number."):
        self.message = message

class FactorialError(Exception):
    def __init__(self,message):
        self.message = ("You can't calculate factorial of negative number")




class Fraction:
    def  __init__(self,numerator,denominator):
        self.numerator = numerator
        self.denominator = denominator


    #Euclidean Algorythm : GCD (Greatest common divisor)
    def gcd(self):
        numerator = self.numerator
        denominator = self.denominator
        while denominator !=0:
            rest = numerator%denominator
            numerator = denominator
            denominator = rest

        return numerator

    #Least Common multiple
    def lcm(self):
        gcd = Fraction(self.numerator,self.denominator).gcd()
        lcm = (self.numerator * self.denominator) / gcd
        return lcm


    #Irreductible Fraction  s = a/b ; m = a/b , x ; d = x
    def irr(self,format='s'):
        gcd_value = self.gcd()
        num_irr = self.numerator / gcd_value
        denom_irr = self.denominator / gcd_value
        standard_result = str(int(num_irr)) + "/" + str(int(denom_irr))
        decimal_result = num_irr / denom_irr
        if format == 'm':
            return standard_result, decimal_result
        elif format == "d":
            return decimal_result
        else:
            return standard_result

class MathCalculate:
    def __init__(self,a):
        self.a = a

    #Factorial
    def factorial(self):

        #Show an error message if self.a < 0
        if self.a < 0:
            raise FactorialError("You can't calculate Factorial of negative number")


        result = 1

        for i in range(1,self.a +1):
            result *=i
        return result

    #Square root basic method
    def sqart(self):
        if self.a >= 0:
            root = self.a ** 0.5
            return round(root,5)
        else:
            raise RootError("RootError: You can't calculate the Root of a negative number.")


    #Cubic root basic method
    def cubrt(self):
        if self.a < 0:
            raise RootError("RootError: You can't calculate the Root of a negative number.")
        else:
            root = self.a ** (1/3)

            return round(root,5)


    def prime_factors(self):
        factors =[]

        #Divided by 2 as many time possible
        while self.a % 2 == 0:
            factors.append(2)
            self.a //=2

        #Browse throught odd numbers starting from 3 to the Sqrt of self.a
        for i in range(3,int(self.a**0.5) +1,2):
            while self.a %i ==0:
                factors.append(i)
                self.a //=i

        #if self.a > 2 it is a prime factor
        if self.a > 2:
            factors.append(self.a)
        return factors



class Equation:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c


    #First degree equation / format : 2+2x = 4
    def eq1(self):
            if self.a != 0:
                result = (self.c-self.a)/self.b
                return round(result,3)
            else:
                raise NotEquation('NotEquation : This is not an Equation "a" must be < or > 0.')


    #Second degree Equation Format : 2x^2 +5x -3 = 0
    def eq2(self):
        if self.a != 0:
            discriminant = self.b**2 - 4*self.a*self.c
            if discriminant > 0:
                x1 = (-self.b + discriminant **0.5) / (2*self.a)
                x2 = (-self.b - discriminant ** 0.5) / (2*self.a)
                return round(x1,3),round(x2,3)
            elif discriminant == 0:
                x = -self.b / (2*self.a)
                return x
            else:
                return 'No solution'
        else:
            raise NotEquation('NotEquation : Not equation of the second degree.')


    def discriminant(self):
        discriminant = self.b**2 - 4*self.a*self.c
        return discriminant


class Statistic:
    def __init__(self,*args):
        self.numbers = args

    #Average of several numbers
    def average(self):
        return sum(self.numbers) / len(self.numbers)

    #Range of several numbers
    def range(self):
        sorted_numbers = sorted(self.numbers)
        return sorted_numbers[-1] - sorted_numbers[0]

    #Mediane of several numbers
    def median(self):
        sorted_numbers = sorted(self.numbers)
        lenght = len(sorted_numbers)

        #Check if is it odd
        if lenght % 2 == 1:
            median = lenght //2
            return sorted_numbers[median]
        #Else it is even :
        else:
            upper_median = lenght //2
            lower_median = upper_median -1
            return sorted_numbers[lower_median],sorted_numbers[upper_median]

    #Variance
    def variance(self):
        average = sum(self.numbers) / len(self.numbers)
        sum_diff = 0
        for x in self.numbers:
            diff = (x - average)**2
            sum_diff += diff
        variance = sum_diff / len(self.numbers)
        return round(variance,4)

    #Standard Derivation
    def std_derivation(self):
        var = Statistic(*self.numbers).variance()
        result = var ** 0.5
        return round(result,3)

    #Mode
    def mode(self):
        frequence = {}
        for value in self.numbers:
            frequence[value] = frequence.get(value,0)+1

        more_numbers = max(frequence.values())

        #Finds modes by selecting keys for wich the frequency is equal to the highest frequency
        modes = [key for key, freq in frequence.items() if freq == more_numbers]
        return modes



class Geometry:
    def __init__(self,a=None,b=None,radius=None):
        self.a = a
        self.b = b
        self.radius = radius

    def area_trgl(self):
        if self.a is None and self.b is None:
            raise ValueError("class '__main__.Geometry is empty")
        A= self.a * self.b /2
        return A


    def area_rctgl(self):
        if self.a is None and self.b is None:
            raise ValueError("class '__main__.Geometry is empty")
        A = self.a *self.b
        return A

    #2 * (a+b)
    def perim_rctgl(self):
        if self.a is None and self.b is None:
            raise ValueError("class '__main__.Geometry is empty")
        P = 2*(self.a +self.b)
        return P
    #
    def diago_rctgl(self):
        if self.a is None and self.b is None:
            raise ValueError("class '__main__.Geometry is empty")
        diagonal =  (self.a**2 + self.b**2) ** 0.5
        return diagonal

    def area_crcle(self):
        if self.radius is None:
            raise ValueError("Radius must be specified")
        pi = 3.14159
        A = pi * self.radius **2
        return A

    def diameter_crcle(self):
        if self.radius is None:
            raise ValueError("Radius must be specified")
        return 2 *self.radius
