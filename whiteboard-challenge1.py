def has_same_digit_frequency(list1, list2):
    dict1 = {}
    dict2 = {}
    freq = 1
    
    #this for loop should read if a dictionary keyvalue exists, add 1 to the frequencycounter
    #otherwise, make the keyvalue exist
   
    for item in list1:
        if item in dict1:
            dict1[item] = freq + 1
        else:
            dict1[item] = freq

    for item in list2:
            if item in dict2:
                dict2[item] = freq + 1
            else:
                dict2[item] = freq
    
    for values in dict1.keys():
        if dict1 == dict2:
            return True
        else:
            return False


print(has_same_digit_frequency([1,2,3,4],[1,2,3,4]))
print(has_same_digit_frequency([5], [7,8]))


        


