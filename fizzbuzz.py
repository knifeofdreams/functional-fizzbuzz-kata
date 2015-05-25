def fizzbuzz():
    return map(lambda number: fizzbuzz_lambdas[number % 15](number), range(1,101))

def const(constant):
    def return_const(x):
        return lambda number: x
    return return_const(constant)

def concat(f, g):
    return lambda number: f(number) + g(number)

id_ = lambda number: str(number)
fizz_ = const("Fizz")
buzz_ = const("Buzz")
fizzbuzz_ = concat(fizz_, buzz_)

fizzbuzz_lambdas = [fizzbuzz_, id_, id_, fizz_, id_, buzz_, fizz_, id_, id_, fizz_, buzz_, id_, fizz_, id_, id_]