print("-" * 15)
print("Task 1:")  # Task1. Lambda Add & Multiply
summed = lambda x: x + 15
multiply = lambda x, y: x * y

print(summed(10))
print(multiply(6, 8))


print("-" * 15)
print("Task 2:")  # Task2. Lambda generator


def func_generator(n):
    return lambda x: x * n


result2 = func_generator(2)
print(f"Double the number of 22 = {result2(22)}")
result2 = func_generator(3)
print(f"Triple the number of 22 = {result2(22)}")
result2 = func_generator(4)
print(f"Quadruple the number of 22 = {result2(22)}")
result2 = func_generator(5)
print(f"Quintuple the number of 22 = {result2(22)}")
result2 = func_generator(2)


print("-" * 15)
print("Task 3: ")  # Task 3. Tuple Sorting
given_list = [("English", 88), ("Science", 90), ("Maths", 97), ("Social sciences", 82)]
print("Original list of tuples:\n", given_list)
sorted_list = sorted(given_list, key=lambda x: x[1])
print("Sorted list of tuples:\n", sorted_list)


print("-" * 15)
print("Task 4: ")  # Task 4. Dictionary Sorting
given_list = [
    {"make": "Nokia", "model": 216, "color": "Black"},
    {"make": "Mi Max", "model": "2", "color": "Gold"},
    {"make": "Samsung", "model": 7, "color": "Blue"},
]
print("Original list of dictionaries:\n", given_list)
sorted_list = sorted(given_list, key=lambda x: x["color"])
print("Sorted list of dictionaries:\n", sorted_list)


print("-" * 15)
print("Task 5: ")  # Task 5. IntegerFilter
given_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Given list of integers:\n", given_list)
even_list = list(filter(lambda x: x % 2 == 0, given_list))
print("Even list of integers:\n", even_list)
odd_list = list(filter(lambda x: x % 2 == 1, given_list))
print("Odd list of integers:\n", odd_list)


print("-" * 15)
print("Task 6: ")  # Task 6. Square & Cube
given_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Given list of integers:\n", given_list)
squared_list = list(map(lambda x: x**2, given_list))
print("Squared list of integers:\n", squared_list)
cubed_list = list(map(lambda x: x**3, given_list))
print("Cubed list of integers:\n", cubed_list)


print("-" * 15)
print("Task 7: ")  # Task 7. String Start Check
start_check = lambda x: x[0] == "A"
# OR start_check = lambda x: True if x.startswith('A') else False
print('Does "Apple and Banana" starts with "A"?')
print(start_check("Apple and Banana"))
print('Does "Banana and Apple" starts with "A"?')
print(start_check("Banana and Apple"))


print("-" * 15)
print("Task 8: ")  # Task 8. Date Time Extractor
import datetime

now = datetime.datetime.now()
print(now)
year = lambda x: x.year
month = lambda x: x.month
day = lambda x: x.day
t = lambda x: x.time()
print(year(now))
print(month(now))
print(day(now))
print(t(now))


print("-" * 15)
print("Task 9: ")  # Task 9. Fibonacci
from functools import reduce

fibo = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1])
print("Fibonacci series upto 2:\n", fibo(2))
print("Fibonacci series upto 5:\n", fibo(5))
print("Fibonacci series upto 8:\n", fibo(8))
print("Fibonacci series upto 11:\n", fibo(11))


print("-" * 15)
print("Task 10: ")  # Task 10. Array Intersection
arr1 = [1, 2, 3, 5, 7, 8, 9, 10]
arr2 = [1, 2, 4, 8, 9]
print("First array: ", arr1)
print("Second array: ", arr2)
inter_arr = list(filter(lambda x: x in arr1, arr2))
print("Intersection of arrays: ", inter_arr)


print("-" * 15)
print("Task 11: ")  # Task 11. Rearrange Pos/Neg
arr = [-1, 2, -3, 5, 7, 8, 9, -10]
print("Orginal array: ", arr)
p_n_arr = sorted(arr, key=lambda x: 0 if x == 0 else -1 / x)
print("Rearranged array: ", p_n_arr)


print("-" * 15)
print("Task 12: ")  # Task 12. Odd/Even Count
arr = [1, 2, 3, 5, 7, 8, 9, 10]
odd_ctr = len(list(filter(lambda x: x % 2 != 0, arr)))
even_ctr = len(list(filter(lambda x: x % 2 == 0, arr)))
print("Given array: ", arr)
print("Number of even numbers: ", even_ctr)
print("Number of odd numbers: ", odd_ctr)


print("-" * 15)
print("Task 13: ")  # Task 13. Add lists
arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
arr3 = list(map(lambda x, y: x + y, arr1, arr2))
print("Original arrays:\n", arr1, "\n", arr2)
print("Arrays sum:\n", arr3)


print("-" * 15)
print("Task 14: ")  # Task 14. Divisible by 19 or 13
arr = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
arr13_19 = list(filter(lambda x: x % 19 == 0 or x % 13 == 0, arr))
print("Orinal array:\n", arr)
print("Numbers %13 or %19:\n", arr13_19)
