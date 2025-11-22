"""
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list

"""

num = list(range(1,11))
old_list = num[0:5]
print("Extracted first five elements:",old_list)
old_list.reverse()
print("Reversed extracted elements:",old_list)