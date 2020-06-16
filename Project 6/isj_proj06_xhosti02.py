#!/usr/bin/env python3

#Adam Hostin
#27.3.2018
#proj č.6 ISJ(skriptovacie jazyky)

from itertools import permutations

def first_nonrepeating (s):
    """:returns first unique letter """
    if isinstance(s,str):
        if (len(s)==0 or (s[0]=='\t') or (s[0]==' ')):
            return None
        order = []
        counts = {}
        for x in s:
            if x in counts:
                counts[x] += 1
            else:
                counts[x] = 1
                order.append(x)
        for x in order:
            if counts[x] == 1:
                return x
        return None
    else:
        return None

def combine4(lst,result):
    """:returns: list of expresions and their value is equel to result"""
    sg=['+', '-', '*', '/']
    newsg=permutations(sg,3)
    newlst=permutations(lst,4)
    newlst=list(newlst)
    newsg=list(newsg)
    test=[]
    brackets=[]
    s=''
    retvalue=[]
    retvalueidx=0
    for i in newlst:
        for j in newsg:
            brackets=[]
            test=[]
            test.append(i[0])
            test.append(j[0])
            test.append(i[1])
            test.append(j[1])
            test.append(i[2])
            test.append(j[2])
            test.append(i[3])
            try:
                s=''.join(str(e) for e in test)
                if eval(s)==result:
                    retvalue.append(s)
            except ZeroDivisionError:
                continue

            brackets=test[:]
            #0
            brackets.insert(0,'(')
            brackets.insert(4,')')
            try:
                s=''.join(str(e) for e in brackets)
                if eval(s)==result:
                    retvalue.append(s)
            except ZeroDivisionError:
                continue
            brackets=test[:]
            #1
            brackets.insert(0,'(')
            brackets.insert(4,')')
            brackets.insert(6, '(')
            brackets.insert(10, ')')
            try:
                s=''.join(str(e) for e in brackets)
                if eval(s)==result:
                    retvalue.append(s)
            except ZeroDivisionError:
                continue
            brackets=test[:]
            #2
            brackets.insert(4,'(')
            brackets.insert(8,')')
            try:
                s=''.join(str(e) for e in brackets)
                if eval(s)==result:
                    retvalue.append(s)
            except ZeroDivisionError:
                continue
            brackets=test[:]
            #3
            brackets.insert(2,'(')
            brackets.insert(6,')')
            try:
                s=''.join(str(e) for e in brackets)
                if eval(s)==result:
                    retvalue.append(s)
            except ZeroDivisionError:
                continue
            brackets=test[:]
            #4
            brackets.insert(0,'(')
            brackets.insert(6,')')
            try:
                s=''.join(str(e) for e in brackets)
                if eval(s)==result:
                    retvalue.append(s)
            except ZeroDivisionError:
                continue
            brackets=test[:]
            #5
            brackets.insert(0,'(')
            brackets.insert(0,'(')
            brackets.insert(5,')')
            brackets.insert(8,')')
            try:
                s=''.join(str(e) for e in brackets)
                if eval(s)==result:
                    retvalue.append(s)
            except ZeroDivisionError:
                continue
            brackets=test[:]
            #6
            brackets.insert(0,'(')
            brackets.insert(3,'(')
            brackets.insert(7,')')
            brackets.insert(7,')')
            try:
                s=''.join(str(e) for e in brackets)
                if eval(s)==result:
                    retvalue.append(s)
            except ZeroDivisionError:
                continue
            brackets=test[:]
            #7
            brackets.insert(2,'(')
            brackets.insert(8,')')
            try:
                s=''.join(str(e) for e in brackets)
                if eval(s)==result:
                    retvalue.append(s)
            except ZeroDivisionError:
                continue
            brackets=test[:]
            #8
            brackets.insert(2,'(')
            brackets.insert(2,'(')
            brackets.insert(7,')')
            brackets.insert(10,')')
            try:
                s=''.join(str(e) for e in brackets)
                if eval(s)==result:
                    retvalue.append(s)
            except ZeroDivisionError:
                continue
            brackets=test[:]
            #9
            brackets.insert(2,'(')
            brackets.insert(5,'(')
            brackets.insert(9,')')
            brackets.insert(10,')')
            try:
                s=''.join(str(e) for e in brackets)
                if eval(s)==result:
                    retvalue.append(s)
            except ZeroDivisionError:
                continue

            test=[]
            brackets=[]

    return list(set(retvalue))




print(combine4([1,1,1,1],2))