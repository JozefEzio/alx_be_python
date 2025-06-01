pattern=int(input('Enter the size of the pattern: '))
rows=pattern
if(pattern>0):
    while rows>0:
        for i in range(pattern):
            print('*',end="")
        rows-=1
        print()
else:
    print("Please enter a positive integer.")    
    