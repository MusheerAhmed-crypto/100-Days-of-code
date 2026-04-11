def first_fit_decreasing(items, capacity):
    items.sort(reverse=True)
    
    bins = []  
    for item in items:
        placed = False
        
        
        for i in range(len(bins)):
            if bins[i] >= item:
                bins[i] -= item
                placed = True
                break
        
       
        if not placed:
            bins.append(capacity - item)
    
    return len(bins)



items = [5 , 9 , 2 , 4 , 7 , 1 , 3 , 6 , 8]
capacity = 10

print("Minimum bins needed:", first_fit_decreasing(items, capacity))