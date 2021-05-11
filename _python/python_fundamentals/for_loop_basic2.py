def func(a):
    for i in range(4):
        if(a[i]>0):
            a[i]="biggie"
    return a
print(func([-5,1,2,-3]))

def func(list):
    sum=0
    for i in range(len(list)):
        if(list[i]>0):
            sum=sum+1
    list.pop()
    list.append(sum)
    return list
print(func([1,2,3,4,-2]))

def func(a):
    sum=0
    for i in range(len(a)):
        sum+=a[i]
    return sum
print(func([1,2,3,4,5]))    

def func(a):
    sum=0
    for i in range(len(a)):
        sum+=a[i]
    return sum/len(a)
print(func([1,2,3,4,5]))    

def func(a):
    return len(a)
print(func([1,2,3,4,5]))    

def func(a):
    min=a[0]
    if not a:
        return False
    else:
        for i in range(1,len(a)):
            if(a[i]<min):
                min=a[i]
    return min
print(func([1,2,-5,4,5]))    

def func(a):
    max=a[0]
    if not a:
        return False
    else:
        for i in range(1,len(a)):
            if(a[i]>max):
                max=a[i]
    return max
print(func([1,2,-5,4,5]))    

def func1(a):
    max=a[0]
    min=a[0]
    sum=0
    newarr=[]
    if not a:
        return False
    else:
        for i in range(1,len(a)):
            sum+=list[i]
            if(list[i]>max):
                max=list[i]
            if(list[i]<min):
                min=list[i]
    avg=sum/len(list)
    newarr.append("max is: {}".format(max))
    newarr.append("min is: {}".format(min))
    newarr.append("sum is: {}".format(sum))
    newarr.append("avg is: {}".format(avg))
    return newlist
print(func1([1,2,-5,4,5]))  

def func2(a):
    dictionary={
        "sumTotal": sum(a),
        "average": sum(a)/len(a),
        "minumum": min(a),
        "maximum": max(a),
        "length":len(a),
    }
    return dictionary
a = [37, 2,1,-9]
print(func(a))

Treversing [

    def reverse_list(a):
    for i in range(len(a)/2):
        a[i], a[len(a)-1-i] = a[len(a)-1-i], arr[i]
            return a
        print (reverse_list([37,2,1,9]))

x = 4
y = 5

print(f"x: {x}, y: {y}")
x,y : y,x
print 
(f"x: {x}, y: {y}")



]
