def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if (swapped == False):
            break

if __name__ == "__main__":
    arr = [27, 15, 35, 32, 22, 11, 100]

    bubbleSort(arr)

    print("Sorted array:")
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")
print()

# binary_search
def binary_search(a, value):
    n = len(a)
    first, last = 0, n - 1

    while first <= last:
        middle = (first + last) // 2
        if a[middle] == value:
            print('Элемент найден')
            print(middle)
            first = last + 1
        elif a[middle] < value:
            first = middle + 1
        else:
            last = middle - 1
            print('элемент не найден')

binary_search([1, 23, 34, 56, 55, 66], 55)
