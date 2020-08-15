def fibonacci_series_r(present_term, next_term, term_count):  # Using Recursion
    if term_count > 0:
        print(present_term, " ", end="")
        fibonacci_series_r(next_term, (present_term + next_term), (term_count - 1))
    else:
        print("")


def fibonacci_series(term_count):
    present_term = 0
    next_term = 1
    while term_count > 0:
        print(present_term, " ", end="")
        temp = present_term + next_term
        present_term = next_term
        next_term = temp
        term_count -= 1
    print("")


def fibonacci_term_r(present_term, next_term, term_count):  # Using Recursion
    if term_count > 1:
        return fibonacci_term_r(next_term, (present_term + next_term), (term_count - 1))
    else:
        return present_term


def fibonacci_term(term_count):
    present_term = 0
    next_term = 1
    while term_count > 1:
        temp = present_term + next_term
        present_term = next_term
        next_term = temp
        term_count -= 1
    return present_term


def is_fibonacci(term_checked):
    present_term = 0
    next_term = 1
    while term_checked >= next_term:
        temp = present_term + next_term
        present_term = next_term
        next_term = temp
    if present_term == term_checked:
        return True
    else:
        return False


def main():  # Driver Method
    t = int(input("Enter Number of terms: "))
    fibonacci_series(t)
    f = fibonacci_term(t)
    print(f"The '{t}'th term is {f}")
    ch = int(input("Enter number to be checked: "))
    print(is_fibonacci(ch))


if __name__ == "__main__":
    main()
