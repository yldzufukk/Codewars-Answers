def str_count(strng, letter):
    
    counter = 0
    
    for i in strng:
        if i == str(letter):
            counter = counter + 1

    return counter