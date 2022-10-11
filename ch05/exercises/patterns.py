# part 1

def star_pyramid():
  rows = int(input("How many rows would you like in your star pyramid: "))
  for i in range(1, rows + 1): 
    print(i * "*")
star_pyramid()


# part 2

def rstar_pyramid():
  rrows = int(input("How many rows would you like in your reverse star pyramid: "))
  for i in range(1, rrows + 1):
    print(rrows * "*")
    rrows = rrows - 1
rstar_pyramid()