def bubble_sort(list):
    sorted = False
    while sorted is False:
        sorted = True
        temp = 0
        for i in range(len(list)-1):
            if list[i] > list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
                sorted = False
    return list

def selection_sort(list):
    for i, value in enumerate(list):
        min_index = i

        for j, value in enumerate(list[i+1:], start=i+1):
            if value < list[min_index]:
                min_index = j

        list[i], list[min_index] = list[min_index], list[i]

    return list 


def insertion_sort(list):
    for i, value in enumerate(list[1:], start=1):
        key = value
        j = i - 1
        while j >= 0 and list[j] > key:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = key
    return list
