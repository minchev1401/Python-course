# 1. Сортиране - Bubble Sort: Имплементирайте алгоритъм за Bubble 
# Sort и тествайте със списък от цели числа.

print("\nBubble Sort\n")

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):

        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        if not swapped:
            break
        
my_list = [123, 15, 255, 32, 63, 78]
bubble_sort(my_list)

print("The sorted list is:")
for num in my_list:
    print(num, end=" ")
    
    
#  2. Selection Sort: Имплементирайте алгоритъма за сортиране 
# Selection Sort

print("\nSelection Sort\n")

def selection_sort(list):
    n = len(list)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if list[j] < list[min_index]:
                min_index = j
        
        list[i], list[min_index] = list[min_index], list[i]


my_list = [123, 15, 255, 32, 63, 78]
selection_sort(my_list)

print("Sorted list is:")
for num in my_list:
    print(num, end=" ")
    
# 3. Insertion Sort: Създайте функция, която използва алгоритъма 
# Insertion Sort за сортиране на масив от числа.

print("\nInsertion_sort\n")

def insertion_sort(list):
    
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key


my_list = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(my_list)

print("Sorted list is:")
for num in my_list:
    print(num, end=" ")
    




