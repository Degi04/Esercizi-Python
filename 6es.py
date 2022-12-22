#De Gironimo Matteo 5A


import math

def print_handshakes(people):
    length = len(people)
    for i in range(len(people)):
        for j in range(len(people)-1):
            print(people[0]+" shakes hands with "+people[j+1]+"\b")
        people.pop(0)
    return (math.factorial(length)/(math.factorial(2)*math.factorial(length-2))) 


assert print_handshakes(['Alice', 'Bob']) == 1
assert print_handshakes(['Alice', 'Bob', 'Carol']) == 3
assert print_handshakes(['Alice', 'Bob', 'Carol', 'David']) == 6