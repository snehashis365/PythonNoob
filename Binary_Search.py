from MyMods import utils

ob = utils()


def main():
    n = int(input("Enter number of elements: "))
    arr = []
    print("Enter elements: ")
    for i in range(0, n):
        arr.append(int(input()))
        i += 1

    # arr = ob.bubble_sort(arr)
    item = int(input("Enter Search item: "))
    i = ob.binary_search(arr, item, False)
    print("Printing....")
    if i >= 0:
        print(f"Found at {i}")
    else:
        print("Not found")
    print(arr)


if __name__ == '__main__':
    main()
