def fizzbuzz():
    return map(lambda number: fizzbuzz_lambdas[number % 15](number), range(1,101))

def const(constant):
    def return_const(x):
        return lambda number: x
    return return_const(constant)

def concat(f, g):
    return lambda number: f(number) + g(number)

def multiples_of(n):
    return map(lambda i: i * n, range(1, 10))

def substract(list_from, what_list):
    return list(set(list_from) - set(what_list))

def take(n, list):
    return list[:n]

def repeat(value, times):
    return [value] * times

def for_all(value, function):
    return dict(zip(value, repeat(function, len(value))))

def combine_dicts(*dict_args):
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result

multiples_of_3 = take(4, multiples_of(3))
multiples_of_5 = take(2, multiples_of(5))
multiples_of_both = [0]
others = substract(range(1,15), multiples_of_3 + multiples_of_5)

id_ = lambda number: str(number)
fizz_ = const("Fizz")
buzz_ = const("Buzz")
fizzbuzz_ = concat(fizz_, buzz_)

fizzbuzz_lambdas = combine_dicts(
    for_all(multiples_of_3, fizz_),
    for_all(multiples_of_5, buzz_),
    for_all(multiples_of_both, fizzbuzz_),
    for_all(others, id_)
)