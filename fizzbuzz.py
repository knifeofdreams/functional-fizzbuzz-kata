def fizzbuzz_of_n(number):
    if (number % 3 == 0 and number % 5 == 0):
        return "FizzBuzz"
    elif (number % 3 == 0):
        return "Fizz"
    elif (number % 5 == 0):
        return "Buzz"
    else:
        return str(number)


def fizzbuzz(number = 100):
    if number < 1:
        return []

    return fizzbuzz(number - 1) + [fizzbuzz_of_n(number)]