#calculator pgm
a=int(input("Enter the first numbrer: "))
b=int(input("Enter the second number: "))

def add(x,y):
    return x+y
def sub(x,y):
    return x-y

print("Select operation.")
print("1.Add")
print("2.Subtract")

choice=input("Enter choice(1/2): ")
if choice=='1':
    print(a,"+",b,"=",add(a,b))
elif choice=='2':
    print(a,"-",b,"=",sub(a,b))
else:
    print("Invalid input")

