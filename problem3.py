# Max Zinski
# Problem 3

import time
import random
from functools import reduce

def main():
    numbers = [1,2,8,3,1,1]
    max_num = max_number(numbers)
    print(f"Maximum number using max_number function. Numbers: {numbers}. max. value: {max_num}")

    maximum_value = reduce(lambda a, b: max(a,b), numbers)
    print(f"Maximum number using reduce expression. Numbers: {numbers}, max. value: {maximum_value}")

    run_experiment()

# list_of_numbers: list of floats or integers
# return: maximum value from the list or None if the input is not valid.
def max_number(list_of_numbers):
    if not isinstance(list_of_numbers, list) or len(list_of_numbers) == 0:
        print(f"Invalid input. Could not find the maximum number. Returning None.")
        return None

    max_val = float('-inf')
    for el in list_of_numbers:
        if type(el) not in {float, int}:
            print(f"{el} was not a valid type. Valid types are floats or integers. Will not compare this element to the largest known value currently.")
            continue
        max_val = max(max_val, el)

    return max_val

"""
Both methods, reduce expression and max_number function have the same runtime, O(n) where n is the number of elements in the list.
Experiment to see which method, the reduce expression or the max_number function, is faster.
This function generates ten datasets of integers, each with a size of 1000, with each integer betweenn -1000 and 1000.
It then finds the maximum number within each dataset using both methods and records their execution times.
The method with the lower execution time is considered to be the faster method.
"""
def run_experiment():
    max_number_total_time = 0
    reduce_expression_total_time = 0

    for i in range(10):
        nums = random.sample(range(-1000, 1000), 1000)

        # calculate time for max_number() to execute
        max_number_start = time.time()
        max_number(nums)
        max_number_end = time.time()
        max_number_total_time += (max_number_end - max_number_start)

        # calculate time for the reduce expression to execute
        reduce_expression_start = time.time()
        reduce(lambda a, b: max(a,b), nums)
        reduce_expression_end = time.time()
        reduce_expression_total_time += (reduce_expression_end - reduce_expression_start)

    # calculate average execution times in milliseconds
    max_number_avg_time_ms = 1000 * (max_number_total_time / 10)
    reduce_expression_avg_time_ms = 1000 * (reduce_expression_total_time / 10)

    if max_number_avg_time_ms < reduce_expression_avg_time_ms:
        print(f"Finding the maximum number using the max_number function ({max_number_avg_time_ms} ms) was faster than using the reduce expression ({reduce_expression_avg_time_ms} ms).")
    elif reduce_expression_avg_time_ms < max_number_avg_time_ms:
        print(f"Finding the maximum number using the reduce expression ({reduce_expression_avg_time_ms} ms) was faster than using the max_number function ({max_number_avg_time_ms} ms).")
    else:
        print(f"Using the reduce expression and the max_number function to find the maximum number took the same amount of time: {reduce_expression_avg_time_ms} ms.")

if __name__ == "__main__":
    main()