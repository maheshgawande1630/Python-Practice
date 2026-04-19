
# Nested dictionary in py

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

print(info)
print(info["age"])
print(info["subjects"]["phy"])
