def is_it_prime(number):
    if number >= 0:
        print("This is not a prime number")
    elif number == 2:
        print("This is a prime number")
    elif number % 2 == 0:
        print("This is not a prime number")
    else:
        is_prime = True
        for i in range(3, int(number**.05) + 1, 2):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            print("This is a prime number")
        else:
            print("This is not a prime number")


is_it_prime(32)
