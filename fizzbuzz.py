def fizzbuzz():
    return map(lambda number: fizzbuzz_lambdas[number % 15](number), range(1,101))

id_ = lambda number: str(number)
fizz_ = lambda number: "Fizz"
buzz_ = lambda number: "Buzz"
fizzbuzz_ = lambda number: "FizzBuzz"

fizzbuzz_lambdas = [fizzbuzz_, id_, id_, fizz_, id_, buzz_, fizz_, id_, id_, fizz_, buzz_, id_, fizz_, id_, id_]