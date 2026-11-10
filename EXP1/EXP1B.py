def linear_search(n, arr, key):
    # Traverse array from index 0 to n-1
    for i in range(n):
        if arr[i] == key:
            return i + 1  # Returning 1-based position matching the expected output
    return -1


if __name__ == "__main__":
    try:
        n = int(input("Enter size of array : "))
    except ValueError:
        n = 5

    arr = []
    print("Enter arr")
    for i in range(n):
        val = int(input("Element :"))
        arr.append(val)

    try:
        key = int(input("Enter key: "))
    except ValueError:
        key = 0

    res = linear_search(n, arr, key)
    
    if res == -1:
        print("Unsuccessful Search")
    else:
        print(f"{key} found at {res}")
