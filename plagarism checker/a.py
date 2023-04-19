#difflib module provides different functions and classes which are used to compare the data sets
#sequencematcher is function in difflib which is used to compare two strings or files

from difflib import SequenceMatcher

# string1="sravani"
# string2="sravani"
# match=SequenceMatcher(None,string1,string2)
# result=match.ratio()*100
# print(result)
with open('text1.txt') as file1, open('text2.txt') as file2:
    f1=file1.read()
    f2=file2.read()
    match=SequenceMatcher(None,f1,f2)
    res=match.ratio()*100
    print(res)