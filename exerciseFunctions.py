def highest_even(li):
    max = 0
    for item in li:
        if item % 2 == 0 and item > max:
            max += item
    return max

print(highest_even([10,2,3,4,8,11]))

# def highest_even2(li):
#     even = []
#     for item in li:
#         if item % 2 == 0:
#             even.append(item)
#     return max(even)

# print(highest_even2([10,2,3,4,8,11]))


