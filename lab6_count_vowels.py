"""

6. Count Vowels
Write a function count_vowels() that takes a string as a parameter and returns the number of vowels (a, e, i, o, u) in the string.

count_vowels("hello")  # returns 2
count_vowels("world")  # returns 1
count_vowels("Python")  # returns 1
"""

#CODE 
#YOUR
#FUNCTION BELOW HERE

def count_vowels(word):
  sum = 0
  for let in word:
    if let == 'a':
      sum += 1
    if let == 'e':
      sum += 1
    if let == 'i':
      sum += 1
    if let == 'o':
      sum += 1
    if let == 'u':
      sum += 1
    if let == 'A':
      sum += 1
    if let == 'E':
      sum += 1
    if let == 'I':
      sum += 1
    if let == 'O':
      sum += 1
    if let == 'U':
      sum += 1
  return(sum)
    
# OK













"""
++++++++++++++++++++
don't code below here
++++++++++++++++++++++
"""
if __name__ == "__main__":
  x = input("Enter in a string to count the vowels of: \n")
  print(count_vowels(x))