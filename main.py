from typing import List


def twoSum(num_list, target):
    for i in range(len(num_list)):
        for j in range(i + 1, len(num_list)):
            if num_list[i] + num_list[j] == target:
                answer_list = [i, j]
                return [i, j]


num_list = list(map(int, input("nums = ").split()))
target = int(input("Enter target : "))

answer_list = twoSum(num_list, target)
print("Output:", answer_list)
