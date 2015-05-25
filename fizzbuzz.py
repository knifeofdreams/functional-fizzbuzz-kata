def fizzbuzz():
    return map(lambda number: fizzbuzz_lambdas[number % 15](number), range(1,101))

def const(constant):
    def return_const(x):
        return lambda number: x
    return return_const(constant)

id_ = lambda number: str(number)
fizz_ = const("Fizz")
buzz_ = const("Buzz")
fizzbuzz_ = const("FizzBuzz")

fizzbuzz_lambdas = [fizzbuzz_, id_, id_, fizz_, id_, buzz_, fizz_, id_, id_, fizz_, buzz_, id_, fizz_, id_, id_]