# Loop Idioms - Finding the largest value

largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)

print('After', largest_so_far)


# finding the smallest value test

# smallest = None
# print('Before:', smallest)
# for num in [3, 41, 12, 9, 74, 15]:
#     if smallest is None or num < smallest:
#         smallest = num
#         print('Loop', num, smallest)
# print('Smallest:', smallest)
