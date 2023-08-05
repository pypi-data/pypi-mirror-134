# number-utils

A library to perform various operations on prime numbers.

### Installation

```Shell
pip install number-utils
```

### Usage

```Python
>>> import number_utils
>>> dir(number_utils)
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', 
'__package__', '__path__', '__spec__', 'are_mutually_prime', 'factor_pairs', 'factors', 
'highest_power', 'is_prime', 'mutually_prime_factor_pairs', 'number_of_divisors', 
'number_of_factor_pairs', 'number_of_mutually_prime_factor_pairs', 'prime_factorise', 
'prime_factors', 'prime_over', 'prime_under', 'primes', 'primes_between', 'primes_under', 
'sum_of_divisors']
>>>
>>> # Examples
>>> from number_utils import is_prime, are_mutually_prime, prime_factorise
>>> is_prime(101)
True
>>> are_mutually_prime(24, 77)
True
>>> prime_factorise(21600, show=True)
2^5 * 3^3 * 5^2
[(2, 5), (3, 3), (5, 2)]
>>>
>>> help(prime_factorise)
Help on function prime_factorise in module number_utils.primes:

prime_factorise(n, show=False)
    Prime factorisation.
    
    If `show` is True, print an expression of the form:
    a^p * b^q * c^r
    where a, b, c, etc. are prime factors of n and p, q, r, etc. are
    their powers.
    
    Return a list of tuples of prime factor and power.
>>>
>>> help(number_utils.highest_power)
Help on function highest_power in module number_utils.primes:

highest_power(m: int, n: int)
    Highest power of a prime m in n!
    
    Formula: Sum of greatest integers contained in (n / m^i), where i
    is 1, 2, 3, etc.
```
