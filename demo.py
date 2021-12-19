def add(x, y):
    """Indirect font-locking makes embedded syntax highlighting easy:

    >>> def test(x): # Here's a function
    ...     return add(x, x)

    >>> [test(x) for x in range(3)]
    [0, 2, 4]

    >>> try:
    ...     print(add("a", 2.0))
    ... except Exception:
    ...     print("Error!")
    Error!
    """
    return x + y
