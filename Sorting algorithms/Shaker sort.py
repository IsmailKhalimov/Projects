def shaker_sort(nums):
    swapped = True
    l = len(nums)
    b = 0
    while swapped:
        swapped = False
        for i in range(b, l-1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                swapped = True
        l -= 1
        for i in range(l-1, b, -1):
            if nums[i] < nums[i-1]:
                nums[i], nums[i-1] = nums[i-1], nums[i]
                swapped = True
        b += 1
list_of_nums = [4, 1, 2, 7, 3]
shaker_sort(list_of_nums)
print(list_of_nums)
