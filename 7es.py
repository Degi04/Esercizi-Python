#De Gironimo Matteo 5A


import random 

def shuffle(values):
    if len(values)==0:
        pass
    else:
        rand = random.randint(0,len(values)-1)
        for i in range(len(values)):
            temp = values[rand]
            values[rand] = values[i]
            values[i] = temp

random.seed(42)

for i in range(10):
    testData1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shuffle(testData1)

assert len(testData1) == 10

assert testData1 != [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

assert sorted(testData1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

testData2 = []
shuffle(testData2)
assert testData2 == []