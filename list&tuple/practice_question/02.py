# check weather the list contains palindrome of element or not

list1=[1,3,1]

copy_list1=list1.copy()
copy_list1.reverse()


if (list1==copy_list1):
    print("It is palindrome")
else:
    print("It is not palindrome")
