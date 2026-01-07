def sum(a,b):
    print("Hey i am summing")
    c=a+b
    global z # please modify global z variable
    z=20 #This will refer gloabal z and not to create a local variable  
    return c
z=5
print(sum(5,5))
print(z)

