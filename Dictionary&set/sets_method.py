# Methods in sets

set1={1,2,3,4}
set2={2,4,5}
set3={2,4,5,6,7,7}


set1.add(7)     #adds an element
set1.remove(7)  #removes an element
set3.clear()    #empties the set

print(set1.union(set2))        # combine both set and values and return new    
print(set1.intersection(set2)) #return common values in both sets
set2.pop()                     #removes random value
print(set2)
