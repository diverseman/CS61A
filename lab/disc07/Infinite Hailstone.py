


def hailstone(n):
    """Yields the elements of the hailstone sequence starting at n.
       At the end of the sequence, yield 1 infinitely.

    >>> hail_gen = hailstone(10)
    >>> [next(hail_gen) for _ in range(10)]
    [10, 5, 16, 8, 4, 2, 1, 1, 1, 1]
    >>> next(hail_gen)
    1
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
      yield 1
      yield from hailstone(n)
    elif n % 2 == 0:
      yield int(n)
      yield from hailstone(n//2)
    else:
      yield int(n)
      yield from hailstone(n * 3 + 1)
if __name__=='__main__':
   import doctest
   doctest.testmod()