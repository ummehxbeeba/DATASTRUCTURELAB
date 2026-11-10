def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high
    
    while i < j:
        while i <= high and arr[i] <= pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[low], arr[j] = arr[j], arr[low]
    return j
def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)
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
    quick_sort(arr, 0, n - 1)
    print("Sorted Array: " + " ".join(map(str, arr)))
