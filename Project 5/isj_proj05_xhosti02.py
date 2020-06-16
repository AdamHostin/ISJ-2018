#!/usr/bin/env python3

#Adam Hostin, xhosti02
#27.3.2018
#proj č.4 ISJ(skriptovacie jazyky)

import re
from math import factorial


class Polynomial:
    """object pracujuci s polynomami"""

    def __init__(self, *coefficients,**dic):
        """ input: list,tuple alebo dictionary
            output: list
        """


        # ak je zadany tupple tak ho convertuje na list
        if (len(coefficients)==0 and len(dic)>0):

            coefficients=[]
            exp = []  # prazdny list pre exponenty
            base = []  # prazdny list pre hodnoty
            for dic in dic.items():
                if isinstance(dic[0], str) == 0 or re.search(r'^x[0-9]+$', dic[0]) == 0 or isinstance(dic[1],int) == 0:  # kontroluje spravny tvar dictionary
                    raise ValueError()
                else:
                    exp.append(dic[0][1:])  # pridava exponent
                    base.append(dic[1])  # pridava zaklad

            exp, base = (list(t) for t in
                         zip(*sorted(zip(exp, base))))  # zoraduje

            i = 0  # pocitadlo exponentov
            e = 0  # pocitadlo zakladov
            while i <= int(exp[-1]):
                if i == int(exp[e]):  # ak bol exponent v p;vodnom liste
                    coefficients.append(int(base[e]))  # pridava exponent
                    e += 1
                else:
                    coefficients.append(0)  # pridava 0
                i += 1



        # ak je zadany na vstupe list pride do __int__ ako prvy prvok tupplu
        elif (isinstance(coefficients[0], list)):
            #do coefficients priradi prvy prvok tupplu
            coefficients=coefficients[0]

        # ak je zadany tupple tak ho convertuje na list
        elif (isinstance(coefficients, tuple)):
            coefficients=list(coefficients)

        self.coefficients = coefficients

    def __pow__(self, power):
        """
        umocnuje polynom
        :param power: exponent
               self.coefficients: list tvoreny z clenov polynomu
        :return: umocneny polynom
        """

        z=[]
        i=0
        j=0
        tmp=0
        #implementacia bynomickej vety
        for j in range(power+1):
           y=self.coefficients[0]**(power-j)
           x=self.coefficients[1]**(j)
           tmp=factorial(power)/(factorial(power-j)*factorial(j))
           z.append(int(tmp*x*y))

        return Polynomial(z)


    def __add__(self, other):
        """
        scitavanie polynomov
        :param other:  list tvoreny z clenov polynomu
               self.coefficients: list tvoreny z clenov polynomu
        :return: sucet 2 polynomov
        """


        # ulozi si vacsi a mensi polynom
        if len(self.coefficients) > len(other.coefficients):
            big = self.coefficients[:]
            small = other.coefficients[:]
        else:
            big = other.coefficients[:]
            small = self.coefficients[:]

        i = 0
        #scitava jednotlivy prvky kym sa neminu prvky mensieho polynomu
        while i < len(small):
            big[i] += small[i]
            i += 1

        return (Polynomial(big))


    def derivative(self):
        """
        derivuje
        :param: self.coefficients:list tvoreny z clenov polynomu
        :return:zderivovany polynom
        """
        derived_coeffs = []
        exponent = 1
        #prechadza jednotlive prvky zacina od druheho a nasoby ich exponentom
        for i in range(1, len(self.coefficients)):
            derived_coeffs.append(self.coefficients[i] * exponent)
            exponent += 1

        return (Polynomial(derived_coeffs))



    def __eq__(self, other):
        """
        porovnava 2 polynomi
        :param other: list tvoreny z clenov polynomu
               self.coefficients: list tvoreny z clenov polynomu
        :return: pravodivostna hodnota
        """

        #doplni polynom nulami ak nemaju rovnaku dlzku
        if len(self.coefficients) > len(other.coefficients):
            big = self.coefficients[:]
            small = other.coefficients[:]

        else:
            big = other.coefficients[:]
            small = self.coefficients[:]
            i=0
        for i in range(len(big)-len(small)):
            small.append(0)
        #porovnava polynomi
        if big == small:
            return True
        else:
            return False



    def at_value(self,*value):
        """
        pocita hodnotu polynomu v bode x ak su zadane 2 hodnoty vrati ich rozdiel
        :param value: 1 alebo 2 hodnoty v bode x
               self.coefficients: list tvoreny z clenov polynomu

        :return: hodnota polynomu v danom bode alebo rozdiel 2 hodnot
        """

        j=0
        sumary=0
        if len(value)==1: #ak bol zadany len jeden polynom
            for i in self.coefficients: #scitava polynom
                k=0
                tmp=1
                for k in range(j):
                    tmp=tmp*value[0] #umocnuje clen na danu mocniny
                sumary=sumary+(tmp*i) #nasoby umocneny clen koeficientom
                j=j+1
            return sumary
        else: #ak boli zadane dva polynomi
            #pocita prvy
            for i in self.coefficients:
                k=0
                tmp=1
                for k in range(j):
                    tmp=tmp*value[0]
                sumary=sumary+(tmp*i)
                j=j+1
            j=0
            sumary2=0
            #pocita ddruhy
            for i in self.coefficients:
                k=0
                tmp=1
                for k in range(j):
                    tmp=tmp*value[1]
                sumary2=sumary2+(tmp*i)
                j=j+1
            #vrati ich rozdiel
            return sumary2-sumary





    def __str__(self):
        """
        formatuje vystup
        :param: self.coefficients:list tvoreny z clenov polynomu
        :return: retazec vyhovujuci assertu
        """
        self.coefficients = self.coefficients[::-1]

        string=""
        j=0
        value=0
        for value in self.coefficients:
            exp=len(self.coefficients)-j-1
            k=0
            #kontrolujem ci sucet predchadzajucich argumentov je 0
            my_sum = 0
            for k in range(j):
                my_sum=my_sum+self.coefficients[k]
            #osetrujem vsetko vsetko co ma napadlo
            if my_sum == 0 and value !=0:

                if exp==1:
                    if value==-1:
                        string = '- x'
                    elif value==1:
                        string = 'x'
                    elif int(value) < 0:
                        string ='- ' + str(abs(value)) + 'x'
                    else:
                        string = str(value) + 'x'
                elif exp==0:
                    if int(value) < 0:
                        string ='- ' + str(abs(value))
                    else:
                        string = str(value)
                else:
                    if value==-1:
                        string = '- x^' + str(exp)
                    elif value==1:
                        string = 'x^' + str(exp)
                    elif int(value) < 0:
                        string ='- ' + str(abs(value)) + 'x^' + str(exp)
                    else:
                        string = str(value) + 'x^' + str(exp)
            else:
                if exp == 1:
                    if value==-1:
                        string = string + ' - x'
                    elif value==1:
                        string = string + ' + ' + 'x'

                    elif int(value) > 0 and j>0:
                        string = string + ' + ' + str(value) + 'x'

                    elif int(value) < 0:
                        string = string + ' - ' + str(abs(value)) + 'x'
                elif exp == 0:
                    if int(value) < 0:
                        string =string+ ' - ' + str(abs(value))
                    elif value==0:
                        pass
                    else:
                        string =string + ' + ' + str(value)


                else:
                    if value==-1:
                        string = string + ' - x^' + str(exp)
                    elif value==1:
                        string = string + ' + ' + 'x^' + str(exp)
                    elif exp==0 and value !=0:
                        string = string + ' - ' + str(abs(value))

                    elif int(value) > 0 and j>0:
                        string = string + ' + ' + str(value) + 'x^' + str(exp)

                    elif int(value) < 0:
                        string = string + ' - ' + str(abs(value)) + 'x^' + str(exp)
            j += 1

        if string=='':
            string='0'

        return string

assert str(Polynomial(0,1,0,-1,4,-2,0,1,3,0)) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x"
assert str(Polynomial([-5,1,0,-1,4,-2,0,1,3,0])) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x - 5"
assert str(Polynomial(x7=1, x4=4, x8=3, x9=0, x0=0, x5=-2, x3= -1, x1=1)) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x"
assert str(Polynomial(x2=0)) == "0"
assert str(Polynomial(x0=0)) == "0"
assert Polynomial(x0=2, x1=0, x3=0, x2=3) == Polynomial(2,0,3)
assert Polynomial(x2=0) == Polynomial(x0=0)
assert str(Polynomial(x0=1)+Polynomial(x1=1)) == "x + 1"
assert str(Polynomial([-1,1,1,0])+Polynomial(1,-1,1)) == "2x^2"
pol1 = Polynomial(x2=3, x0=1)
pol2 = Polynomial(x1=1, x3=0)
assert str(pol1+pol2) == "3x^2 + x + 1"
assert str(pol1+pol2) == "3x^2 + x + 1"
assert str(Polynomial(x0=2).derivative()) == "0"
assert str(Polynomial(x3=2,x1=3,x0=2).derivative()) == "6x^2 + 3"
assert str(Polynomial(x3=2,x1=3,x0=2).derivative()) == "6x^2 + 3"
assert str(Polynomial(x3=2,x1=3,x0=2).derivative().derivative()) == "12x"
pol4 = Polynomial(x3=2,x1=3,x0=2)
assert str(pol4.derivative()) == "6x^2 + 3"
assert str(pol4.derivative()) == "6x^2 + 3"

assert str(Polynomial(x0=-1,x1=1)**1) == "x - 1"
assert str(Polynomial(x0=-1,x1=1)**2) == "x^2 - 2x + 1"
pol3 = Polynomial(x0=-1,x1=1)
assert str(pol3**4) == "x^4 - 4x^3 + 6x^2 - 4x + 1"
assert str(pol3**4) == "x^4 - 4x^3 + 6x^2 - 4x + 1"


assert Polynomial(-2, 3, 4, -5).at_value(0) == -2
assert Polynomial(x2=3, x0=-1, x1=-2).at_value(3) == 20
assert Polynomial(x2=3, x0=-1, x1=-2).at_value(3, 5) == 44
pol5 = Polynomial([1, 0, -2])
assert pol5.at_value(-2.4) == -10.52
assert pol5.at_value(-2.4) == -10.52
assert pol5.at_value(-1, 3.6) == -23.92
assert pol5.at_value(-1, 3.6) == -23.92
