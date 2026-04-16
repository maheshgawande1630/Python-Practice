#WAF to print all elements in list

def print_list(list,idx=0):

    if(idx==len(list)):
        return

    print(list[idx])
    print_list(list,idx+1)

cities=["akola","akot","kolhapur","pune","thane","mumbai"]

print_list(cities)