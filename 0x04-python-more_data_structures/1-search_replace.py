#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    if search < len(new_list) and search > -len(new_list):
        if search > 0:
            new_list[search-1] = replace
        else:
            new_list[search] = replace
    return new_list
        
