
A = [1, 2, 3, 4, 5]

# helper function for the first_solution that returns the product of the array.


def array_product(A):

    result = 1

    for i in range(len(A)):

        result *= A[i]

    return result

# Solution takes O(n) time because we are only looping through the array once.
# Side note: we loop through the array twice so we are making 2n iterations but
# 2n = O(n).


def first_solution(A):

    n = len(A)
    result = [0] * n
    product = array_product(A)

    for i in range(n):

        result[i] = product / A[i]

    return result

# What if we can't use division?

# Solution is O(n^2)


def naive_no_division(A):

    n = len(A)
    result = [1] * n

    for i in range(n):
        for j in range(n):

            if i == j:
                continue
            else:
                result[i] *= A[j]

    return result


print(naive_no_division(A))
