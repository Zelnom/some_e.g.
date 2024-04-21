def prime_num(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
def sum_digit(num):
    result = 0
    while num != 0:
        result += num % 10
        num //= 10
    return result

def sum_digit_str(num):
    str_value = str(num)
    suma = 0
    for i in str_value:
        suma += int(i)
    return suma



if __name__ == '__main__':
    print(sum_digit(234))
    print(sum_digit_str(234))