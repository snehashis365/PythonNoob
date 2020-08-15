from MyMods import num_utils
get=num_utils()
size=int(input("Enter Size: "))
for i in range(size):
    for j in range(size-i):
        print("  ",end="")
    for j in range(i+1):
        print("%4d"%get.nCr(i,j),end='')
    print("")
