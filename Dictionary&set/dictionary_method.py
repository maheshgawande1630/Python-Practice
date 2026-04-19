# Dictionary Methods

info={

"name":"Mahesh",
"age":19,
"hobies":("playing cricket","listening music"),

"subjects":{         #nested dictionary
    "phy":98,
    "che":99,
    "math":78
}

}

print(list(info.keys())) #returns all keys
print(list(info.values())) # returns all values
print(list(info.items()))  #returns all (key,value) pairs as tuples
print(info.get("age")) #return the key according to value
info.update({"city":"Akola"}) #inserts the specified items to the dictionary
print(info)
