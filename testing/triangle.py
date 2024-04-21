def triangle(length):
    if length % 2 == 0:
        length -= 1
    result = ""
    for i in range(1, length + 1, 2):
        result += " " * ((length - i)//2) + "#" * i + "\n"
    return result

if __name__ == '__main__':
    print(triangle(10))