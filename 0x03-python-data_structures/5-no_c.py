def no_c(my_string):
    for i in len(my_string):
        if my_string[i] != 'c' and my_string[i] != 'C':
            new += my_string[i]
    return new
