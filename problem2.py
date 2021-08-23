# Max Zinski
# Problem 2

import time
import random
import temperature_converter as tc

temperatures = [-32.0, 0.0, 1.0, 10.0, 32.0, 50.3, 88.8, 101.0]

# use map to convert a list of temperatures from fahrenheit to celsius
m = map(tc.convert_fahr_to_cels, temperatures)

# use list comprehension to make the same conversion
l = [tc.convert_fahr_to_cels(x) for x in temperatures]

# What is the time complexity of each approach? Devise and conduct a benchmarking experiment to determine if one is faster than the other in practice.
"""
Both approaches have a time complexity of O(n) where n is the number of temperatures in the list.
For my experiment, I'll generate ten samples (each with 1000 integers) of random temperatures in fahrenheit within the range -450 and 1000, then convert them to celsius using BOTH map conversion
and list comprehension. I've written two methods, map_conversion and list_comprehension_conversion which can track and return the execution time for the operations.
I'll calculate the average execution time for both conversion methods and the method with the lower execution time will be deemed faster.
"""
# temperatures: a list of temperatures
# provide_time_metrics: boolean representing whether or not we care about the time metrics for this operation
# return: a tuple like (list of converted temperatures, None if provide_time_metrics is False otherwise the execution time)
def map_conversion(temperatures, provide_time_metrics=False):
    start_time = time.time()
    m = map(tc.convert_fahr_to_cels, temperatures)
    end_time = time.time()
    
    if provide_time_metrics: 
        execution_time = end_time - start_time
    else:
        execution_time = None
    
    return (temperatures, execution_time)

def list_comprehension_conversion(temperatures, provide_time_metrics=False):
    start_time = time.time()
    l = [tc.convert_fahr_to_cels(x) for x in temperatures]
    end_time = time.time()

    if provide_time_metrics:
        execution_time = end_time - start_time
    else:
        execution_time = None
    
    return (temperatures, execution_time)

def run_experiment():
    total_map_time = 0
    total_list_comprehension_time = 0
    for i in range(10):
        # generate a list of 1000 random numbers between -450 and 1000: https://www.geeksforgeeks.org/generating-random-number-list-in-python/
        temps = random.sample(range(-450, 1000), 1000)
        m = map_conversion(temps, True)
        total_map_time += m[1]

        l = list_comprehension_conversion(temps, True)
        total_list_comprehension_time += l[1]

    # calculate average times and convert to ms
    average_map_time_ms = 1000 * (total_map_time / 10)
    average_list_comprehension_time_ms = 1000 * (total_list_comprehension_time / 10)

    if average_map_time_ms > average_list_comprehension_time_ms:
        print(f"Map conversion took longer! Average time using map conversion: {average_map_time_ms} ms. Average time using list comprehension: {average_list_comprehension_time_ms} ms.")
    elif average_list_comprehension_time_ms > average_map_time_ms:
        print(f"List comprehension took longer! Average time using map conversion: {average_map_time_ms} ms. Average time using list comprehension: {average_list_comprehension_time_ms} ms.")
    else:
        print(f"Both conversion methods took the same amount of time: {average_map_time_ms} ms")

if __name__ == "__main__":
    run_experiment()