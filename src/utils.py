### QUICKSORT ###

def quicksort(A: list, l: int, r: int, states: list[list]) -> None:

    if l < r:
        x = A[r]
        i = l - 1
        for j in range(l, r):
            if A[j] <= x:
                i += 1
                A[i], A[j] = A[j], A[i]
                states.append(A[:])
        A[i+1], A[r] = A[r], A[i+1]
        states.append(A[:])
        q = i + 1
        quicksort(A, l, q-1, states)
        quicksort(A, q+1, r, states)