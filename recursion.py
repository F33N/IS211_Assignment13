def fibonacci(number):
  if number <= 1:
    return number
  else:
    return fibonacci(number-1) + fibonacci(number-2)

def gcd(a, b):
    if b == 0:
        return a
    else:
        r= a % b
        return gcd(b, r)


def compareTo(s1, s2):
    n = 0
    if len(s1) == 0 or len(s2) == 0:
        if len(s1) == 0 and len(s2) == 0:
            return 0
        elif len(s1) != 0 and len(s2) == 0:
            return 1
        elif len(s1) == 0 and len(s2) != 0:
            return -1

    if s1[n] < s2[n]:
        return -1

    elif s1[n] == s2[n]:
        return compareTo(s1[n + 1:], s2[n + 1:])

    elif s1[n] > s2[n]:
        return 1
    else:
        return 0

def main():
    number = int(input("Enter integer number: "))
    print("The 9th element of the Fibonnaci sequence is : {}".format(fibonacci(number)))
    s1 = input("Enter the first string: ")
    s2 = input("Enter the second string: ")
    print(compareTo(s1, s2))
    a = int(input("Enter the first integer: "))
    b = int(input("Enter the second integer: "))
    print("The GCD is {} ".format(gcd(a, b)))

if __name__ == "__main__":
    main()