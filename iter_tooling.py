#! /usr/bin/env python3

from itertools import accumulate, repeat, islice

def take(n, iter):
    """ Takes the first n return values from an iterator """
    return list(islice(iter, n))

def iterate(f, x):
    """ Iterates over the output of a function, recursively re-applying it to the new output"""
    return accumulate(repeat(x), lambda fx, _: f(fx))


if __name__ == "__main__":
    def add1sq(x):
        return (x + 1) ** 2 

    print("Returning first 10 results of add1sq()")

    print(take(10, iterate(add1sq, 1)))
