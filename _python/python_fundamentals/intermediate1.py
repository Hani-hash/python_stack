import random
def randInt(min=0, max=100):
    num = random.random() * (max-min) + min
    if min <= max and max > 0:
    return round(num)
print(randInt())
print(randInt(max=50))
print(randInt(min=50))
print(randInt(min=50, max=500))
print(randInt(min50, max500))



# import random
# def randInt(min=0, max=100):
#     num = random.random() * (max-min) + min
#     if (min<max):
#         return "min is less than max"
#     if (max>500):
#         return "max is greater" 
# print(randInt(min=50, max=600))           

