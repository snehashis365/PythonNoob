class utils:

    def __init__(self):
        pass

    def isPrime(self, num):
        i, count = 2, 0
        flag = True
        while i <= num // 2:
            if num % i == 0:
                flag = False
                break
            i += 1
        return flag

    def isEven(self, num):
        return num % 2 == 0

    def isOdd(self, num):
        return num % 2 != 0

    def factorial(self, num):
        p=1
        for x in range(1,num+1) :
           p = p * x
        return p

    def nCr(self, n, r):
        if r>0:
            return int(self.factorial(n)/( self.factorial(r) * self.factorial(n - r) ) )
        else:
            return 1

    def digit_sum(self, num):
        temp, s = num, 0
        while temp>0:
            s+= temp % 10
            temp = temp // 10
        return s

    def num_reverse(self, num):
        temp, r = num, 0
        while temp>0:
            r = (r * 10) + (temp % 10)
            temp = temp // 10
        return r

    def bubble_sort(self, arr):
        n = len(arr)
        for i in range(0, (n - 1)):
            flag = True
            for j in range(0, (n - i - 1)):
                if arr[j] > arr[j + 1]:
                    flag = False
                    temp = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j + 1] = temp

            if flag:
                break
        return arr

    def insertion_sort(self, arr):
        n= len(arr)
        for i in range(1,n):

            temp = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > temp:
                    arr[j + 1] = arr[j]
                    j-= 1
            arr[j + 1] = temp

        return arr

    def linear_search(self, arr, sk):
        for i in range(0, len(arr)):
            if arr[i] == sk:
                return i
        return -1

    def binary_search(self, arr, sk, sorted=None):
        if sorted is not None and not sorted:
            print("Sorting...")
            arr = self.bubble_sort(arr)
        ub, lb = len(arr), 0
        while lb <= ub:
            mid = (ub + lb) // 2
            if arr[mid] == sk:
                return mid
            elif arr[mid] > sk:
                ub = mid
            else:
                lb = mid
        return -1