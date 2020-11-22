def find_uniq(arr):
    if arr[0] != arr[1]: #when the unique num is the first or second one:
        if arr.count(arr[0]) == 1:
            return arr[0]
        else:
            return arr[1]
    else:
        for elem in arr:
            if elem != arr[0]:
                return elem
