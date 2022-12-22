#De Gironimo Matteo 5A


def maximum(t):
    t.sort()
    return t[len(t)-1]

def minimum(t):
    t.sort()
    return t[0]

def somma(t):
    somma = 0
    for i in t:
        somma+=i
    return somma


def prod(t):
    prod = 1
    for i in t:
        prod*=i
    return prod

def moda(t):
    conto = 0
    conto_max = 0
    ris = 0
    for i in t:
        for j in range(len(t)):
            if i == t[j]:
                conto +=1
        if(conto > conto_max):
            ris = i
            conto_max = conto
        conto = 0
    return ris 


def avg(t):
    return somma(t)/len(t)

def median(t):
    t.sort()
    if(len(t)%2==0):
        return (t[int(len(t)/2)-1]+t[int((len(t)/2)+1)-1])/2
    else:
        return t[int((len(t)+1)/2)-1]


t = [1, 2, 3, 4, 5, 7]
print(maximum(t))
print(minimum(t))
print(somma(t))
print(prod(t))
print(round(avg(t),2))    
print(median(t))

assert maximum(t) == 7
assert minimum(t) == 1
assert somma(t) == 22
assert prod(t) == 840
assert round(avg(t), 2) == 3.67
assert median(t) == 3.5

assert moda([1, 2, 3, 1, 2, 1, 1, 1, 2]) == 1
assert moda([1, 2, 3, 3, 3, 1, 2, 1, 2, 3, 3, 3]) == 3


import random
random.seed(42)
t = [3, 7, 10, 4, 1, 9, 6, 2, 8]
for _ in range(5):
  random.shuffle(t)
  assert median(t) == 6