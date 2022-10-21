def multiply(x=0,y=0):
  result = 0
  for i in range(x):
    result += y   
  return result 

x = int(input("Enter number:"))
y = int(input("Enter number:"))
num = multiply(x,y)
print(num)

def expo(b=0,exp=0):
  result = 1 
  for i in range(exp):
    result *= b
  return result

b = int(input("Enter number:"))
exp = int(input("Enter number:"))
e = expo(b,exp)
print(e)

def square(n):
  result = 0 
  for i in range(n):
    result = result + n
  return result 

n = int(input("Enter number:"))
v = square(n)
print(v)