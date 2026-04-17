#Create a new file "practice.txt" using py and add new data,after that replace some words by another

#1st part of program

# with open("practice.txt","r") as f:
#     data = f.read()

#     new_data  = data.replace("Java","Python")
#     print(new_data)

#     with open("practice.txt","w") as f:
#         f.write(new_data)


#2nd part of program

#search for word learning
word="learning"
with open("practice.txt","r") as f:
    data = f.read()
    if(data.find(word) !=-1):
        print("Found")
    else:
            print("not found")