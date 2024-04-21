def perfect_square(number):
    sqrt = number ** (1/2)
    # print(type(sqrt))
# sau facem  is_int = int(sqrt) == sqrt
    # if number
    is_int = int(sqrt) == sqrt
    return is_int

if __name__ == '__main__':
    print(perfect_square(9))
    print(perfect_square(10))

