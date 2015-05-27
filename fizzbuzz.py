import itertools

def fizzbuzz(n = 100):
    return take(n, fizzbuzz_generator())

def fizzbuzz_generator():
    return itertools.imap(lambda function, i: function(i), itertools.cycle(fizzbuzz_lambdas.values()), itertools.count(1,1))

def const(constant):
    return lambda number: constant

def concat(f, g):
    return lambda number: f(number) + g(number)

def multiples_of(n):
    return itertools.count(n, n)

def substract(list_from, what_list):
    return list(set(list_from) - set(what_list))

def take(n, generator):
    return list(itertools.islice(generator, 0, n))

def repeat(value, times):
    return [value] * times

def for_all(value, function):
    return dict(zip(value, repeat(function, len(value))))

def combine_two_dicts(lhs, rhs):
    result = lhs.copy()
    result.update(rhs)
    return result

def combine_dicts(*dict_args):
    return reduce(combine_two_dicts, dict_args, {})

def return_(function):
    return lambda x: function(x)

multiples_of_3 = take(4, multiples_of(3))
multiples_of_5 = take(2, multiples_of(5))
multiples_of_both = [15]
others = substract(range(1,15), multiples_of_3 + multiples_of_5)

it_ = lambda number: str(number)
fizz_ = const("Fizz")
buzz_ = const("Buzz")
fizzbuzz_ = concat(fizz_, buzz_)

fizzbuzz_lambdas = combine_dicts(
    for_all(multiples_of_3, return_(fizz_)),
    for_all(multiples_of_5, return_(buzz_)),
    for_all(multiples_of_both, return_(fizzbuzz_)),
    for_all(others, return_(it_))
)