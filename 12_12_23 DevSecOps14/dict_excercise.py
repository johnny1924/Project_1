# write a python script to generate and print a dictionanery that ocntains a number
# (between 1 and n) in the form (x, x*x)
# sample dict n as input :
# expected output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# def generate_square_dict(n):
#     square_dict = {}
#     for x in range(1, n+1):
#         square_dict[x] = x*x
#     return square_dict
#
# n = int(input("Enter the value of n: "))
#
# result_dict = generate_square_dict(n)
# print(result_dict)


# write a python program to map two lists into a dictionary
# abs = ['a', 'b', 'c', 'd']
# nums = [1, 2, 3]

# dict1 ={}
# for i in range(len(abs)):
   # if i < len(nums):
        # dict1[abs[i]] = nums[i]
    # else:
       # dict1[abs[i]] = None
# print(dict1)

# items = [
   # {'item': 'item1', 'amount': 400},
   # {'item': 'item2', 'amount': 300},
   # {'item': 'item3', 'amount': 750}
#]

# counter = {}
# for d in items:
    # for k,v in d.items():
        # print(k,v)
   # values = list(d.values())
   # if values[0] in list(counter.keys()):
       # counter[values[0]] = values[1] + counter[values[0]]
    # else:
       # counter[values[0]] = values[1]

# print(counter)
