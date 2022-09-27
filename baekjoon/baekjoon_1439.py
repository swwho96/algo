import re
zero_r = re.compile('0+')
one_r = re.compile('1+')
word = input()
print(min(len(zero_r.findall(word)), len(one_r.findall(word))))