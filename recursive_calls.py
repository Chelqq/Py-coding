def test(N):
    num = N
    if num > 0:
        print(str(num)+ " Waos")
        test(num-1)

test(5)
#Waos
print("\nWaos\n")
test(100)