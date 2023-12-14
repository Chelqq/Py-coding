"""
This script does the following:
-Lists the words present in both lists (inner join)
-Lists exclusively the words in the 1st list 
-Lists exclusively the words in the 2nd list 
-Lists the words in the 2 lists
"""

list1_strs = ["hola","X","Chris","Yeezus","Lamar","Lenovo","Github"]
list2_strs = ["AI","Pandas","hola","0","Kendrick","Python","Yeezus"]

l1 = [1,4,6,7,73,4,2,2,44,5,66,1,2,4,5,6,77]
l2 = [1,4,54,6,7,3,5,3,5,6,7,3,324]

# Del duplicates
l1_set = set(l1)
l2_set = set(l2)

union = list( l1_set | l2_set)
union.sort()
print(f"En las 2 listas hay: {union}, despues de remover duplicados")

onlyA = list(l1_set - l2_set)
onlyA.sort()
print(f"Elementos exclusivos de la ista 1: {onlyA}, sin duplicados")

onlyB = list(l2_set - l1_set)
onlyB.sort()
print(f"Elementos exclusivos de la lista 2: {onlyB}, sin duplicados")

intersection =list(l1_set & l2_set)
intersection.sort()
print(f"La interseccion entre las 2 listas de numeros es: {intersection}")

