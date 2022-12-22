#De Gironimo Matteo 5A


import random
#funziona a metà
def gen_pwd(length):    
    caratteri = "abcdefghijklmnopqrstuvzABCDEFGHIJKLMNOPQRSTUVZ0123456789~!@#$%^&*()_+."
    return "".join(random.sample(caratteri,length))

assert len(gen_pwd(7)) == 8 
assert len(gen_pwd(8)) == 8 
from string import ascii_uppercase, ascii_lowercase, digits
special = '~!@#$%^&*()_+.'
pwd = gen_pwd(8)
assert any(c in pwd for c in ascii_uppercase), 'uppercase letter missing'
assert any(c in pwd for c in ascii_lowercase), 'lowercase letter missing'
assert any(s in pwd for s in special), 'special char missing'
assert any(d in pwd for d in digits), 'digit missing'