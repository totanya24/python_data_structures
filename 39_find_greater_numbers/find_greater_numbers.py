def find_greater_numbers(nums):
    """Return # of times a number is followed by a greater number.

    For example, for [1, 2, 3], the answer is 3:
    - the 1 is followed by the 2 *and* the 3
    - the 2 is followed by the 3

    Examples:

        >>> find_greater_numbers([1, 2, 3])
        3

        >>> find_greater_numbers([6, 1, 2, 7])
        4

        >>> find_greater_numbers([5, 4, 3, 2, 1])
        0

        >>> find_greater_numbers([])
        0
    """

    count = 0
    for i in range(len(nums)):
        print('i',i)
        for j in range(i + 1, len(nums)):
            print('j',j)
            if nums[j] > nums[i]:
                print('j',nums[j])
                print('x',nums[i])
                count += 1
    return count

print(find_greater_numbers([6, 1, 2, 7]))