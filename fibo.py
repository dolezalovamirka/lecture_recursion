def recursive_nth_fibo(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    elif number >= 1:
        return recursive_nth_fibo(number - 1) + recursive_nth_fibo(number - 2)


def main():
    vysledek = recursive_nth_fibo(6)
    print(vysledek)
    n = int(input("Zadejte kladne cislo: "))
    fibonacciho_list = []
    for i in range(n):
        fibonacciho_list.append(recursive_nth_fibo(i))
    print(fibonacciho_list)


if __name__ == "__main__":
    main()
