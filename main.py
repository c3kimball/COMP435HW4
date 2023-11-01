# Craig Kimball
# COMP435 HW4
import random


def counting_sort(nums: list):
    """Applies counting sort on nums.
    nums is expected to be a list of ints that are between 0 and 9 inclusive.
    It is in radix sort that will prepare the randomly generated numbers to be sorted for counting_sort"""
    count = [0] * 10 # Initializes count to start at all zeroes
    buffer = [0] * len(nums)

    # first count of each number
    for i in range(len(nums)):
        count[nums[i]] += 1

    # cumulative count
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Sorting nums into buffer
    for i in range(len(nums) - 1, -1, -1): # This for loop iterates starting from the end of nums and stops at the start
        buffer[count[nums[i]] - 1] = nums[i]
        count[nums[i]] -= 1

    return buffer


def generate_random_nums(size: int, low: int, high: int):
    """Generates a list of random numbers between low and high. The amount of numbers generated is = to size.
    To make things simple at first, I will use size = 10, low = 1000, high = 9999"""
    rand_nums = [0] * size
    for i in range(size):
        rand_nums[i] = random.randint(low, high)

    return rand_nums


def main():
    random_numbers = generate_random_nums(10, 1000, 9999)
    print(f"random numbers to be sorted: {random_numbers}")
    nums = [5, 2, 4, 7, 1, 5, 1, 8, 4, 5, 7, 9, 2, 9] # A hardcoded example I used for testing
    print(counting_sort(nums))


if __name__ == "__main__":
    main()