#Dictionary uses for a leetcode problem

mydict = {"num1": 1, "num2": 2, "num3": 3, "num4": 4, "num5": 5}

#accesing the keys in the dict, using a for loop priting the values
for iterr in mydict:
    print(iterr)

#accesing the keys in the dict, using a for loop STORING the values
mylst = []
for iterr2 in mydict:
    mylst.append(iterr2)
print(mylst)

#accesing the VALS in the dict, using a for loop STORING the values
vallst = []
for x in mydict:
    vallst.append(mydict[x])
print(vallst)

#accesing the KEYS AND VALUES in the dict, using a for loop STORING the values
bothlst = []
for y in mydict:
    buffer = []
    buffer.append(y)
    buffer.append(mydict[y])
    bothlst.append(buffer)
print(bothlst)
