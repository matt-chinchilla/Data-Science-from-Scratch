#16a) The big question: How can we be confident our code is correct?
        ## Answer: One way is with "Assert" statements which will throw a "AssertionError"
        ## if the condition is not truthy

assert 1 + 1 == 2
assert 1 + 1 == 2, "1 + 1 should equal 2 but didn't"            # Can add a msg if assertion fails


#16b) Definitely more fun to use "assert" in order to find that functions are doing what you expect them to
def smallest_item(xs):
    return min(xs)

assert smallest_item([10, 20, 5, 40]) == 5
assert smallest_item([1, 0, -1, 2]) == -1


#16c) Another way is to assert things about inputs for our functions
def smallest_item(xs):
    assert xs, "empty list has no smallest item"
    return min(xs)