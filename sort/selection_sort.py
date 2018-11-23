
# 选择排序思路： 给定一个待排序的数组，每一次遍历，从数组中选出最小（或最大）的元素，放在一个新数组中；
# 再从剩余的元素中选出最小（或最大）的元素，以此类推，直至所有的元素都排序完成。

# 时间复杂度： O(n * n)
# 是一个不稳定的排序算法

# 获取数组中，最小元素的索引
def find_smallest(arr):
    smallest_item = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest_item:
            smallest_item = arr[i]
            smallest_index = i

    return smallest_index

# 选择排序算法
def selection_sort(arr):
    newArr = []

    for i in range(len(arr)):
        smallest_index = find_smallest(arr)
        newArr.append(arr.pop(smallest_index))

    return newArr

arr = [5, 3, 6, 2, 10]
print(selection_sort(arr))