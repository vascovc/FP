
def genFibonacci(n):
    """Generate list of first n Fibonacci numbers: [F0, F1, ... Fn-1]."""
    # your code here
    ...


def main():
    # Do tests:
    lst = genFibonacci(10)
    print(lst)      #-> [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    # Check the results we expect.
    # (If a condition fails, the assert statement raises an AssertionError!)

    assert isinstance(lst, list), "lst should be a list"
    assert lst == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    assert genFibonacci(2) == [0, 1]
    assert genFibonacci(6) == [0, 1, 1, 2, 3, 5]

    # If the program reaches this point...
    print("All tests passed!")

    # Let the user try it:
    n = int(input("N? "))
    print("genFibonacci({}) -> {}".format(n, genFibonacci(n)))


# Call main function:
main()

