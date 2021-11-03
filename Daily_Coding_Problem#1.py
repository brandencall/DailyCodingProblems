
A = [10, 15, 3, 7]
k = 17

# Solution runs in O(n^2)


def naive_solution(A, k):

    for i in range(len(A)):
        for j in range(len(A)):

            if i == j:
                continue

            if A[i] + A[j] == k:
                return True

    return False

# Only loops 1 time but still takes O(n^2) time because the difference_arr is of length n


def one_loop_solution(A, k):

    n = len(A)
    difference_arr = [0] * n

    for i in range(n):

        if A[i] in difference_arr:
            return True

        difference_arr[i] = k - A[i]

    return False


print(one_loop_solution(A, k))
