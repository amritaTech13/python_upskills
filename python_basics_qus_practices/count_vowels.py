
import re
str = 'Amrita'

vowels = 'aeiouAEIOU'
# count = sum( [1 for i in str if i in vowels])
# print(f"Number of Vowels in given string is {count}")

vowels = r'[aeiouAEIOU]'
vowel = re.findall(vowels, str)
print(f' no of vowels {len(vowel)}')