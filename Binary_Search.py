from MyMods import list_utils

ob = list_utils()


def main():
    n = int(input("Enter number of elements: "))
    arr = []
    print("Enter elements: ")
    for i in range(0, n):
        arr.append(int(input()))
        i += 1
    isSorted =input("Is the list sorted(Y/N)?")
    item = int(input("Enter Search item: "))
    if isSorted == "Y":
        i = ob.binary_search(arr, item, True)
    else:
        i = ob.binary_search(arr, item, False)
    print("Printing....")
    if i >= 0:
        print(f"Found at {i}")
    else:
        print("Not found")
    print(arr)


if __name__ == '__main__':
    main()
