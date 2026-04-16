#WAF to print the element of the list in a single line (list is parameter)



num=[2,3,2,1,4,67,4,7,3]
cities=["akola","akot","telhara","pune","kolhapur"]


def print_list(list):
    for item in list:
        print(item,end=" ")

print_list(num)
