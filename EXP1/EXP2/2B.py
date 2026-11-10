def selection_sort(n, arr):
    for i in range(n - 1):
        min_val = arr[i]
        min_idx = i
        for j in range(i, n):
            if min_val > arr[j]:
                min_val = arr[j]
                min_idx = j
        # Swap the found minimum element with the first element of the pass
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
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

    selection_sort(n, arr)
