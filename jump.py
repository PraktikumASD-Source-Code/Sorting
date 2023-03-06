import os
os.system("clear")

def jumpSearch(arr, x):

    n = len(arr)

    step = int(n ** 0.5)

    prev = 0

    while arr[min(step, n) -1 ] < 1:
        prev = step
        step += int(n ** 0.5)

        if prev >= n:
            return -1
        
    while arr[prev] < x:
        prev += 1

        if prev == min(step, n):
            return -1

    if arr[prev] == x:
        return prev
    
    return -1

arr = [1, 2, 3, 4, 5]

x = 6

result = jumpSearch(arr, x)

if result != -1:
    print(f"Elemen {x}, ditemukan di index {result}")
else:
    print(f"Elemen {x} tidak ditemukan pada array") 
        

