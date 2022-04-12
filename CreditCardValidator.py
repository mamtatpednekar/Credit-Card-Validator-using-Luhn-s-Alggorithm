# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 22:47:42 2022

@author: Mamta Pednekar
"""

No = str(input("Enter Credit card no"))
creditCardNo = list(No)
oddSum = 0
doubleEvenSum = []
evenSum = 0

for (idx,val) in enumerate(creditCardNo):
    if idx % 2 != 0:
        oddSum = oddSum + int(val)
    else:
        doubleEvenSum.append(int(val)*2)
doubleStringEven = ""
for x in doubleEvenSum:
    doubleStringEven += str(x)

newList = list(doubleStringEven)


for x in newList:
    evenSum += int(x)

if (evenSum + oddSum) % 10 == 0:
    print("Valid Credit Card")
else:
    print("Invalid Credit Card")


    
