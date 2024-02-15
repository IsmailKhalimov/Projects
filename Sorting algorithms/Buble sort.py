def bubble_sort(nums):
    swapped = True
    l = len(nums)
    while swapped:
        swapped = False
        for i in range(l-1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
        l -= 1

list_of_nums = [5, 2, 1, 8, 4]
bubble_sort(list_of_nums)
print(list_of_nums)