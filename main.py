def fibonacci(n):
    if n <= 0:
        return 0, 0
    elif n == 1:
        return 1, 1

    a, b = 0, 1
    total_sum = 1
    for _ in range(2, n + 1):
        a, b = b, a + b
        total_sum += b

    return b, total_sum

def main():
    n = int(input("Enter the term of the Fibonacci sequence to be calculated: "))
    term, total_sum = fibonacci(n)
    print(f"The {n}th term of the Fibonacci sequence is: {term}")
    print(f"The sum of all terms in the sequence up to the {n}th term is: {total_sum}")

if __name__ == "__main__":
    main()
