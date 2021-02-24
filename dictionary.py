## Dictionaries Option 1
#--------------------------------------------------------------------------------
f = open('news.txt', 'r')
wordCount={}
for sentence in f:
    for word in sentence.strip().split():
        if wordCount.has_key(word):
            wordCount[word]=wordCount[word]+1
        else:
            wordCount[word] = 1

print wordCount

g=open('output.txt','w')
#sorted is optional: 'sorted(wordCount.items())' can be replaced with simply 'wordCount.items()'

for k,v in sorted(wordCount.items()):
    g.write(k +': '+ str(v)+'\n')

## Observation: You will notice that one word, e.g., 'Sunday' appears as 1, and then the same word
# but followed by comma 'Sunday,' appears as 1 as well. This is why the sentence needs to be cleaned
# of punctuations, such that 'Sunday' appears as 2 in the example.
#-----------------------------------------------------------------------------------------------

## Dictionaries Option 2
L = ['apple','red','apple','red','red','pear'
from collections import defaultdict
d = defaultdict(int)
for i in L:
...   d[i] += 1
d
defaultdict(<type 'int'>, {'pear': 1, 'apple': 2, 'red': 3})
#---------------------------------------------------------------------------------------------
## Dictionaries Option 3

items = "Whats the simpliest way to add the list items to a dictionary "

stats = {}
for i in items:
    if i in stats:
        stats[i] += 1
    else:
        stats[i] = 1
# bonus
for i in sorted(stats, key=stats.get):
    print("%d◊'%s'" % (stats[i], i))
#---------------------------------------------------------------------------------
Dictionaries Option 4
#-----------------------------------------------------------------------------------
# Program to count the number of each vowel in a string

# string of vowels
vowels = 'aeiou'

# take input from the user
ip_str = input("Enter a string: ")

# make it suitable for caseless comparisions
ip_str = ip_str.casefold()

# make a dictionary with each vowel a key and value 0
count = {}.fromkeys(vowels,0)

# count the vowels
for char in ip_str:
   if char in count:
       count[char] += 1
#------------------------------------------------------------------------------------------------
output:
Enter a string: Hello, have you tried our turorial section yet?
{'e': 5, 'u': 3, 'o': 5, 'a': 2, 'i': 3}
#-------------------------------------------------------------------------------------------------

#Dictionaries option 5
#--------------------------------------------------------------------------------------
# Program to count the number of
# each vowel in a string using
# dictionary and list comprehension

# take input from the user
ip_str = input("Enter a string: ")

# make it suitable for caseless comparisions
ip_str = ip_str.casefold()

# count the vowels
count = {x:sum([1 for char in ip_str if char == x]) for x in 'aeiou'}

print(count)
#-----------------------------------------------------------------------------