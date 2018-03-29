import re

patterns = ['term1', 'term2']

text = 'This is a string with term1, not the other'

for pattern in patterns:
    print("I'm searching for: "+pattern)

    if re.search(pattern,text):
        print("Match!")
    else:
        print("No match!")

print(match.start())

#Exmple2

import re

split_term = '@'
email = 'user@fmail.com'
print(re.split(split_term,email))

#OR we can do:

email = 'user@fmail.com'.split('@')
print(email)

Example 3:
import re

print(re.findall('match', 'test phrase match in middle'))

#Example4:

import re

def multi_re_find(patterns,phrase):

    for pattern in patterns:
        print("Searching for pattern{}".format(pattern))
        print(re.findall(pattern, phrase))
        print('\n')

test_phrase = 'ssddd...ddsss...sssdddd...dsds...sdsd'

test_patterns = ['sd+']   #you can use* or ? or {number inside}

multi_re_find(test_patterns, test_phrase)

##
import re

def multi_re_find(patterns,phrase):

    for pattern in patterns:
        print("Searching for pattern{}".format(pattern))
        print(re.findall(pattern, phrase))
        print('\n')

test_phrase = 'This is a string!! But it has many punctuations. How can i remove it?'

test_patterns = ['[^!.?]+']  #^ to exclude the terms inside[this] |||  '\d+' to get all numbers and '\D+' to get all words and many more!!

multi_re_find(test_patterns, test_phrase)
