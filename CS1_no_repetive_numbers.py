# Problem:
# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

# It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 # Example 1:

# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# Example 2:

# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
def combinations_to_the_total_chosen(i,list_of_integers, total_chosen,length_of_list,combinations_lists = []):
    s = sum(combinations_lists)
    if s == total_chosen:
        print (combinations_lists)
    else:
        while i <= (length_of_list): ## error
        #for i in range(len(list_of_integers)):
            n = list_of_integers[i]
            next_integer = list_of_integers[i+1]
            i =+1
            combinations_to_the_total_chosen(i,next_integer, total_chosen,length_of_list,combinations_lists = [n])

i = 0
i = int(i)
list_of_numbers = str(input("Please eneter numbers to add up to chosen total(example 1 2 5 7):\n"))
# converts intput from string to list
list_of_numbers = list(list_of_numbers.split(" "))
list_of_integers= []
string_used_to_count = ""
for e in list_of_numbers:
    e = int(e)
    list_of_integers.append(e)
    list_of_integers = list(list_of_integers)
for e in list_of_integers:
        e = str(e)
        string_used_to_count = string_used_to_count + e
(string_used_to_count)
# print("string")
# print(string_used_to_count)
# print ("count is")
length_of_list = (len(string_used_to_count))
# print (length_of_list)
total_chosen = int(input("What is the total you would like these numbers combinations to add up to:\n"))
combinations_to_the_total_chosen(i,list_of_integers, total_chosen,length_of_list, combinations_lists = [])