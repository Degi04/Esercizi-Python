#De Gironimo Matteo 5A


def bubble_sort(numbers):
    for j in range(len(numbers)-1):
        for i in range(len(numbers)-1):
            if numbers[i]>numbers[i+1]:
                temp = numbers[i+1]
                numbers[i+1] = numbers[i]
                numbers[i] = temp
    return numbers

assert bubble_sort([2, 0, 4, 1, 3]) == [0, 1, 2, 3, 4]
assert bubble_sort([2, 2, 2, 2]) == [2, 2, 2, 2]