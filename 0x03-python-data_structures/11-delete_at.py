#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list)-1:
        return my_list
    new_list = my_list.copy()
    for i in range(len(new_list)):
        if i == idx:
            my_list[i:] = []
        elif i < idx:
            my_list[i] = new_list[i]
        else:
            my_list.append(new_list[i])
    return my_list
