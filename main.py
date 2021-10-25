import itertools
from fractions import Fraction

blanks = []
answers = []
ops = ['+', '-', '*', '/']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def istrueint(tgt:str)->bool:
    if tgt == '':
        return False
    for elem in tgt:
        if elem not in numbers:
            return False
    return True

def istruefraction(tgt:str)->bool:
    if tgt == '':
        return False
    numleft = 0
    for i in range(0, len(tgt)):
        if tgt[i] == '(':
            numleft = numleft + 1
            numright = 0
            for j in range(len(tgt)-1, i-1, -1):
                if(tgt[j] == ')'):
                    numright = numright + 1
                if numright == numleft:
                    i = j+1
        if i == len(tgt):
            return True
        if tgt[i] != '/' and tgt[i] not in numbers:
            return False
    return True

def hasinside(tgt:str, beg:int, end:int, chr:str):
    numleftparenthe = 0
    for i in range(beg, end+1):
        if tgt[i] == '(':
            numleftparenthe = numleftparenthe + 1
            numrightparenthe = 0
            for j in range(end, i-1, -1):
                if tgt[j] == ')':
                    numrightparenthe = numrightparenthe + 1
                if numrightparenthe == numleftparenthe:
                    i = j+1
        if i == end+1:
            return True
        if tgt[i] != chr and tgt[i] in ops:
            return False
    return True

# Find parenthes like (6) or (10)
def findexcess(tgt:str)->bool:
    for i in range(0, len(tgt)):
        for j in range(i+1, len(tgt)):
            if tgt[i] == '(' and tgt[j] == ')':
                if istrueint(tgt[i+1:j]) or istruefraction(tgt[i+1:j]):
                    return True
    return False

# Find parenthes like 6+(6+(6+6)) or 6*(6*(6*6))
def findexcessaddmult(tgt:str)->bool:
    cntleft = 0
    for i in range(0, len(tgt)-1):
        if tgt[i] == '+' and tgt[i+1] == '(':
            cntleft = cntleft + 1
            r = 0
            cntright = 0
            for j in range(i+1, len(tgt)):
                if tgt[j] == ')':
                    cntright = cntright + 1
                if cntright == cntleft:
                    r = j-1
                    break
            if hasinside(tgt, i+1, j, '+'):
                return True
        if tgt[i] == '*' and tgt[i+1] == '(':
            cntleft = cntleft + 1
            r = 0
            cntright = 0
            for j in range(i+1, len(tgt)):
                if tgt[j] == ')':
                    cntright = cntright + 1
                if cntright == cntleft:
                    r = j-1
                    break
            if hasinside(tgt, i+1, r, '*'):
                return True
    return False

def dfs(idx:int, length:int, numbers:list, tgt:int, remainingleft:int)->None:
    if idx == length-1:
        finalstr = 'Fraction(%d)'%(numbers[0])
        finalstrprn = str(numbers[0])
        for i in range(1, len(numbers)):
            finalstr = finalstr + str(blanks[i-1]) + 'Fraction(%d)'%(numbers[i])
            finalstrprn = finalstrprn + str(blanks[i-1]) + str(numbers[i])
        if remainingleft > 0:
            for i in range(remainingleft):
                finalstr = finalstr + ')'
                finalstrprn = finalstrprn + ')'
        try:
            if(eval(finalstr) == tgt):
                answers.append(finalstrprn + '=%s'%(tgt))
        except ZeroDivisionError:
            pass
        return
    for elem in ops:
        if remainingleft > 0:
            blanks[idx] = ')' + elem
            dfs(idx+1, length, numbers, tgt, remainingleft-1)
        blanks[idx] = elem + '('
        dfs(idx+1, length, numbers, tgt, remainingleft+1)
        blanks[idx] = elem
        dfs(idx+1, length, numbers, tgt, remainingleft)

def calculate(numbers:list, tgt:int)->list:
    for k in range(1, len(numbers)):
        blanks.append('')
    for elem in itertools.permutations(numbers, len(numbers)):
        dfs(0, len(numbers), elem, tgt, 0)
    actans = []
    for elem in answers:
        if elem not in actans and not findexcess(elem) and not findexcessaddmult(elem):
            actans.append(elem)
    return actans