def insertion_sort(a, n, h):
    num_of_move = 0

    for i in range(h, n):
        x = a[i]
        j = i - h

        while j >= 0 and a[j] > x:
            a[j + h] = a[j]
            j -= h
            num_of_move += 1

        a[j + h] = x

    print(num_of_move)


def shell_sort(a, n, h):
    for h_i in h:
        insertion_sort(a, n, h_i)


n = int(input())
a = list(map(int, input().split()))
k = int(input())
h = list(map(int, input().split()))

shell_sort(a, n, h)