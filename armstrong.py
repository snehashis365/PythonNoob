def is_armstrong(num):
    temp, s = num, 0
    while temp > 0:
        s += (temp % 10) ** 3
        temp = temp // 10
    if s == num:
        return True
    else:
        return False


n = int(input("Enter number: "))
if is_armstrong(n):
    print("Armstrong!!")
else:
    print("Not Armstrong")
