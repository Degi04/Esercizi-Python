#De Gironimo Matteo 5A

def find_and_replace(text, old_text, new_text):
    for i in range(len(text)):
        if text[i:i+len(old_text)] == old_text :
            text = text[0:i]+new_text+text[i+len(old_text):len(text)]
    return text

assert find_and_replace('The fox', 'fox', 'dog') == 'The dog'
assert find_and_replace('fox', 'fox', 'dog') == 'dog'
assert find_and_replace('Firefox', 'fox', 'dog') == 'Firedog'
assert find_and_replace('foxfox', 'fox', 'dog') == 'dogdog'
assert find_and_replace('The Fox and fox.', 'fox', 'dog') == 'The Fox and dog.'
assert find_and_replace('THE FOX AND THE DOG', 'fox', 'dog') == 'THE FOX AND THE DOG'
