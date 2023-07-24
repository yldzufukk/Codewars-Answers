def enough(cap, on, wait):
    
    space = cap - on
    
    if space > wait:
        return 0
    
    if space < wait:
        return wait - space
    
    if space == wait:
        return 0
