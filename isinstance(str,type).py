# 1. Basic Data Types
print(isinstance(25, int))          # True (Integer)
print(isinstance(19.99, float))     # True (Decimal)
print(isinstance("Hello", str))     # True (String)
print(isinstance(True, bool))       # True (Boolean)

# 2. Data Structures
print(isinstance([1, 2, 3], list))  # True (List)
print(isinstance((1, 2), tuple))    # True (Tuple)
print(isinstance({1, 2}, set))      # True (Set)
print(isinstance({"a": 1}, dict))   # True (Dictionary)

num=''
while num !='q':
    num=input("enter a number or q ")
    if num.isalpha():
        if num in ['q','Q']:
            print("execution over : ")
            break
        else: 
            print("wrong input try again : ")
            pass
    elif num.isdigit():
        num1=int(num)
        if num1%2==0:
            print("even")
        else:
            print("odd")
    else:
        print("try again")
    