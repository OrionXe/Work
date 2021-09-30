""" Given a text as input, find and output the longest word.
"""
txt=input()
list=txt.split()
longest = max(list, key=len)# key este folosit la sortarea elementelor
print(longest)