#function is a block of code which perform specific task

def calc_sum(n):
    if(n==0):
        return 0
    return calc_sum(n-1)+n

sum=calc_sum(5)
print(sum)
