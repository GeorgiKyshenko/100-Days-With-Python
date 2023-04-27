def prime_number_check(num):
    is_prime = True
    if num == 2 or num == 1:
        print(f"{num} is a prime number.")
    else:
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")


number = int(input("Enter a number: "))
prime_number_check(number)
