from MyMods import utils

util = utils()


def prime_series(start, end):
    for i in range(start, end + 1):
        if (util.isPrime(i)):
            print(i, " ", end="")
    print("")


def main():
    prime_series(10, 30)


if __name__ == '__main__':
    main()
