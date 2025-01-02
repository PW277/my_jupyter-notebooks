#This file is a scratchpad for coding challenges involving lists. It is a WIP.


my_list = [12, 89, 34, 67, 25, 91, 3, 56, 78, 78, 78, 43]
list1 = [1,2,3,4]
list2 = [3,4,5,6]

#Q1 - reverse a list
def reverse_list(my_list):
    #edge case - empty list as input
    if not my_list:
        return []
    
    #initialise left and right pointers for index 0 and index len(list) -1
    left, right = 0, len(my_list) - 1

   
    
    #check first index against last index and loop if true
    while left < right:
         # swap elements
        my_list[left], my_list[right] = my_list[right], my_list[left]
        #increment left, decrement right
        left+=1
        right-=1

    return my_list

print(reverse_list(my_list))

#Q2 - find the max value in a list
def find_max(my_list):
    #edge case - empty list
    if not my_list:
        return None
    #set variable to first item
    max_value = my_list[0]
    #start loop from second index
    for i in my_list[1:]:
        if i > max_value:
            max_value = i
    return max_value

print(find_max(my_list))

#Q3 - remove duplicates from a list

def remove_duplicates(my_list):
    if not my_list:
        return []
    #set for quick lookup
    values_found = set()
    answer_list = []
    for item in my_list:
        if item not in values_found:
            values_found.add(item)
            answer_list.append(item)
    return answer_list
print(remove_duplicates(my_list))

#Q4 - count the occurance of each element in a list
def find_occurances(my_list):
    if not my_list:
        return {}
    value_count = dict()

    for i in my_list:
        value_count[i] = value_count.get(i, 0) + 1
        
    return value_count

print(find_occurances(my_list))
#Q5 find common elements in two lists
def find_common_elements(l1, l2):
    lookup_set = set(l1)
    result_list = []

    for item in l2:
        if item in lookup_set:
            result_list.append(item)
            lookup_set.remove(item)
    return result_list

print(find_common_elements(list1, list2))





# def find_common_elements(l1, l2):
#     lookup_set = set(l1)
#     result_list = []

#     for item in l2:
#         if item in lookup_set:
#             result_list.append(item)
#             lookup_set.remove(item)
#     return result_list
# print(find_common_elements(list1, list2))




# Find common elements between two lists

#check if a list is a sublish of another list
#find the index of an element in a list
# merge two sorted lists
#rotate a list
#find the first non-repeated character in a string
#check if a string is a pallendrome
