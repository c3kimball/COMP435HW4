# Craig Kimball
# COMP435 HW4
import random


def counting_sort(nums: list, exponent: int):
    """Applies counting sort on nums.
    nums is expected to be a list of ints that are between 0 and 9 inclusive.
    It is in radix sort that will prepare the randomly generated numbers to be sorted for counting_sort"""
    count = [0] * 10 # Initializes count to start at all zeroes
    buffer = [0] * len(nums)

    # first count of each number
    for i in range(len(nums)):
        index = nums[i]/exponent # index is which tens place the program is currently working with. starts with ones
        # place then 10's, 100's etc
        count[int(index % 10)] += 1

    # cumulative count
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Sorting nums into buffer
    i = len(nums) - 1 # Need to traverse list backwards
    while i >= 0:
        index = nums[i]/exponent
        buffer[count[int(index % 10)] - 1] = nums[i]
        count[int(index % 10)] -= 1
        i -= 1

    i = 0
    for i in range(0, len(buffer)):
        nums[i] = buffer[i]


def radix_sort(nums: list):
    """Applies Radix sort on a list of numbers.
    Uses countingsort as the main sorting algorithm"""
    max_num = max(nums)
    exp = 1
    while max_num // exp > 0:
        counting_sort(nums, exp)
        exp *= 10


def generate_random_nums(size: int, low: int, high: int):
    """Generates a list of random numbers between low and high inclusive. The amount of numbers generated is equal to
    size. """
    rand_nums = [0] * size
    for i in range(size):
        rand_nums[i] = random.randint(low, high)

    return rand_nums


def main():
    random_numbers = generate_random_nums(10, 0, 9999)
    print(f"Random numbers to be sorted: {random_numbers}")

   # nums = [2, 4, 7, 1, 5, 1, 8, 4, 7, 9, 2, 9] # A hardcoded example I used for testing
    # print(f"Printing fixed list: {counting_sort(nums, 1)}")
    # print(nums)
    print("Applying radix_sort on random_nums...")
    radix_sort(random_numbers)
    print(f"Sorted random_numbers: {random_numbers}")


if __name__ == "__main__":
    main()