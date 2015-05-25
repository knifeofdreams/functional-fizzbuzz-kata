def fizzbuzz(number = 100):
    if number < 1:
        return []

    if (number % 3 == 0 and number % 5 == 0):
        result = "FizzBuzz"
    elif (number % 3 == 0):
        result = "Fizz"
    elif (number % 5 == 0):
        result = "Buzz"
    else:
        result = str(number)

    return fizzbuzz(number - 1) + [result]