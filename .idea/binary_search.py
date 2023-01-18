def selection_sort(array):
    size=len(array)
    for i in range(size-1):

        min=array[i]

        for j in  range(i+1, size):
            if array[j]<min:
                min=array[j]
                array[j],array[i]=array[i],array[j]

    return array

unsorted_array=[29,5,3,87,6,1,110,83,96,8,45,25,92,54,19,57,47,69,93]

print("Sorted Array ")
print(selection_sort(unsorted_array))
