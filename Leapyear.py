# Homework 7 Leapyear.py Alexis Matheson


def checkyear(num):
    if num % 4 and num % 100 and num % 400:
        return True
    else:
        return False


def main():
    year = input("Enter a year you want to test: ")
    try:
        int(year)
        is_year = True
    except:
        is_year = False
        print("The input entered is not valid.")
    if is_year == True:
        checkyear(year)


if __name__ == "__main__":
    main()