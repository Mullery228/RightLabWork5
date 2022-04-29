src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = []


def get_numbers(nums: list):
    for i in range(1, len(src) - 1):
        a = nums[i - 1]
        if nums[i] > a:
            result.append(src[i])
    yield result


print(*get_numbers(src))
