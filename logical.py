age=int(input("enter your age please"))
responses= input("enter whether you have voter id for not").lower()
if (responses in ['yes','y','true','t','i have']):
    flag =1
else :
    flag =0


if (age>=18 and flag==1):
    print("elligible")

elif (age>=18 and flag==0):
    print("apply for voter id you are adult")

else:
    print("not elligible minor")
    

print(True or True)
print(False or True)
print(True or False)
print(False or False)