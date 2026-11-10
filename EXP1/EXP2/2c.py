def insertion_sort(n, arr):
    for i in range(1, n):
        ele = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > ele:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = ele
        # Print array after each pass
        print(f"Pass {i}: " + " ".join(map(str, arr)))


if __name__ == "__main__":
    try:
        n = int(input("Enter size of array: "))
    except ValueError:
        n = 5

    arr = []
    print("Enter arr")
    for i in range(n):
        val = int(input(f"Element :"))
        arr.append(val)

    insertion_sort(n, arr)
