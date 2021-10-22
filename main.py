import itertools

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

def findexcess(tgt:str)->bool:
    for i in range(0, len(tgt)):
        for j in range(i, len(tgt)):
            if tgt[i] == '(' and tgt[j] == ')':
                if istrueint(tgt[i+1:j]):
                    return True
    return False

def dfs(idx:int, length:int, numbers:list, tgt:int, remainingleft:int)->None:
    if idx == length-1:
        finalstr = ''
        finalstr = finalstr + str(numbers[0])
        for i in range(1, len(numbers)):
            finalstr = finalstr + str(blanks[i-1]) + str(numbers[i])
        if remainingleft > 0:
            for i in range(remainingleft):
                finalstr = finalstr + ')'
        try:
            if(eval(finalstr) == tgt):
                answers.append(finalstr + '=%s'%(tgt))
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
        if elem not in actans and not findexcess(elem):
            actans.append(elem)
    return actans
print(calculate([6, 6, 6, 6], 24))