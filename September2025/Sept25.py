numArr = [7, 7, 7]

def second_largest(arr):
    #converting array to set to delete duplication
    myset = set(arr)
    #converting set to list
    sorted_list = list(myset)
    #sorting the list
    sorted_list.sort()
    #returning the second larggest element in the array
    if len(sorted_list) > 1:
        return sorted_list[-2] 
    else :
        return sorted_list[-1]
    
print(second_largest(numArr))