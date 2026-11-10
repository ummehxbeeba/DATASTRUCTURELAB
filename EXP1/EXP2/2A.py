def bubble_sort(n, arr):
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                # Swap adjacent elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        # Print array after each pass
        print(f"Pass {i + 1}: " + " ".join(map(str, arr)))


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

    bubble_sort(n, arr)
