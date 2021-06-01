# Homework 7 FizzBuzz.py Alexis Matheson


def checknum(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num


def main():
    for i in range(101):
        if i == 0:
            continue
        else:
            checknum(i)


if __name__ == "__main__":
    main()