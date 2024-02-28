#ERROR GESTION
class NotEquation(Exception):
    """Equation Error : It is not an equation."""

class RootError(Exception):
    """Root error : You can't calculate a root of negative number."""

class FactorialError(Exception):
    """Factorial Error : You can't calculate factorial of negative number."""




class Fraction:
    def  __init__(self,numerator,denominator):
        self.numerator = numerator
        self.denominator = denominator


    #Euclidean Algorythm : GCD (Greatest common divisor)
    def gcd(self):
        #While denom is different from 0
        while self.denominator !=0:
            #numerator % denominator -> numerator become denominator -> denominator become rest
            rest = self.numerator%self.denominator
            self.numerator = self.denominator
            self.denominator = rest
        #Return the response
        return self.numerator

    #Least Common multiple
    def lcm(self):
        #Call the fonction gcd
        gcd = Fraction(self.numerator,self.denominator).gcd()
        #calculate lcm :
        lcm = (self.numerator * self.denominator) / gcd
        #Return the response
        return lcm


    #Irreductible Fraction  s = a/b ; m = a/b , x ; d = x
    def irr(self,format='s'):
        #Call the fonction gcd
        gcd_value = self.gcd()
        #makes numerator irreductible
        num_irr = self.numerator / gcd_value
        #makes denominator irreductible
        denom_irr = self.denominator / gcd_value
        #Standard result format : x/b
        standard_result = str(int(num_irr)) + "/" + str(int(denom_irr))
        #Decimal result format : 4.675
        decimal_result = num_irr / denom_irr

        #Return a specific format ( decimal or standard or both)
        if format == 'm':
            return standard_result, decimal_result
        elif format == 'd':
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
        #i -> 1 to a +1
        for i in range(1,self.a +1):
            #add *i in result
            result *=i
        #return the response
        return result

    #Square root basic method
    def sqart(self):
        #Verifying if a >= 0
        if self.a >= 0:
            #Calculate the root
            root = self.a ** 0.5
            #Return the root
            return round(root,5)
        #Send a RootError
        else:
            raise RootError("You can't calculate the root of a negative number.")


    #Cubic root basic method
    def cubrt(self):
        #Verifying if a < 0 (Error management
        if self.a < 0:
            #Send a RootError
            raise RootError("You can't calculate the root of a negative number.")
        else:
            # Calculate the cubic root
            root = self.a ** (1/3)
            #Return the root
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
        #Verifying if a is different from 0
            if self.a != 0:
                #Calculate the equation
                result = (self.c-self.a)/self.b
                #Return the result
                return round(result,3)
            else:
                #Send a NotEquation Error
                raise NotEquation('NotEquation : This is not an Equation "a" must be < or > 0.')


    #Second degree Equation Format : 2x^2 +5x -3 = 0
    def eq2(self):
        #Verifying if a is different from 0
        if self.a != 0:
            #Calculate the discriminante
            discriminant = self.b**2 - 4*self.a*self.c
            #Verifying if the discriminant is greater than 0
            if discriminant > 0:
                #Calculate x1 and x2
                x1 = (-self.b + discriminant **0.5) / (2*self.a)
                x2 = (-self.b - discriminant ** 0.5) / (2*self.a)
                #Return x1,x2
                return round(x1,3),round(x2,3)
            #Else if discriminant equals 0
            elif discriminant == 0:
                #Calculate x
                x = -self.b / (2*self.a)
                return x
            #Else there is no solution
            else:
                return 'No solution'
        #Send NotEquation Error
        else:
            raise NotEquation('NotEquation : Not equation of the second degree.')


    def discriminant(self):
        #Calculate the discriminant
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
        #Sort the numbers
        sorted_numbers = sorted(self.numbers)
        return sorted_numbers[-1] - sorted_numbers[0]

    #Mediane of several numbers
    def median(self):
        #Sort the numbers
        sorted_numbers = sorted(self.numbers)
        lenght = len(sorted_numbers)

        #Check if is it odd
        if lenght % 2 == 1:
            #calculate the median
            median = lenght //2
            return sorted_numbers[median]
        #Else it is even :
        else:
            #Calculate the lower and upper median
            upper_median = lenght //2
            lower_median = upper_median -1
            return sorted_numbers[lower_median],sorted_numbers[upper_median]

    #Variance
    def variance(self):
        #Calculate average
        average = sum(self.numbers) / len(self.numbers)
        sum_diff = 0
        for x in self.numbers:
            #calculate difference
            diff = (x - average)**2
            #add in sum_diff , diff
            sum_diff += diff
        #Calculate the variance
        variance = sum_diff / len(self.numbers)
        return round(variance,4)

    #Standard Derivation
    def std_derivation(self):
        #Calculate the variance
        var = Statistic(*self.numbers).variance()
        #Calculate the standard derivation
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
        #Error gestion
        if self.a is None and self.b is None:
            raise ValueError("class '__main__.Geometry is empty")
        #Calculate the area
        A= self.a * self.b /2
        return A


    def area_rctgl(self):
        if self.a is None and self.b is None:
            raise ValueError("class '__main__.Geometry is empty")
        # Calculate the area
        A = self.a *self.b
        return A

    #2 * (a+b)
    def perim_rctgl(self):
        if self.a is None and self.b is None:
            raise ValueError("class '__main__.Geometry is empty")
        # Calculate the perimeter
        P = 2*(self.a +self.b)
        return P
    #
    def diago_rctgl(self):
        if self.a is None and self.b is None:
            raise ValueError("class '__main__.Geometry is empty")
        # Calculate the diagonal
        diagonal =  (self.a**2 + self.b**2) ** 0.5
        return diagonal

    def area_crcle(self):
        if self.radius is None:
            raise ValueError("Radius must be specified")
        pi = 3.14159
        # Calculate the area
        A = pi * self.radius **2
        return A

    def diameter_crcle(self):
        if self.radius is None:
            raise ValueError("Radius must be specified")
        #Return the diameter of the circle
        return 2 *self.radius
        
    def circumference_crcle(self):
        if self.radius is None:
            raise ValueError("Radius must be specified to calculate the diameter")
        #Calculate the diameter
        diameter = Geometry(radius=self.radius).diameter_crcle()
        #pi
        pi = 3.14159
        #Return the circumference :C = pi * d
        return  pi * diameter
        

