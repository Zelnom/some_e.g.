import math

# 1. Numbers divided by x
# 	a. create a function that counts how many numbers can be divided by 3 from 1 to n
# 	b. create a function that counts how many numbers are palindrom from 1 to n (121, 1234321)
# 	c. create a function that counts how many prime numbers are from 1 to n
# 	d. create THREADS to run all 3 functions at the same time
# 	e. create PROCESSES to run all 3 function at the same time


print("Exercise 1 ---- Multithreading")
print("-" * 30)


def div_by_3(n):
    count = 0
    for i in range(0, n + 1):
        if i % 3 == 0:
            count += 1
    return count


def is_palindrome(n):
    count = 0
    for i in range(1, n + 1):
        p = 0
        num = i
        while i != 0:
            p = p * 10 + i % 10
            i = int(i / 10)

        if num == p:
            count += 1
    return count


def is_prime(n):
    count = 0
    for i in range(1, n + 1):
        is_prime = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                count += 1
    return count


def main():
    print(is_palindrome(123))
    print(is_prime(100))


if __name__ == '__main__':
    main()
