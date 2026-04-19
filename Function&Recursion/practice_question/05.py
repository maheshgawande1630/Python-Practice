#WAF to sum of 1st n natural num

def calc_sum(n):
    if(n==0):
        return 0
    return calc_sum(n-1)+n

result=calc_sum(8)
print(result)        