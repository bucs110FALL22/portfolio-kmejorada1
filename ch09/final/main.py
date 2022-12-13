import DogAPI
import CatAPI

#first question will determine what type of fact the user will get
answer = str(input("Do you prefer cats or dogs? (Respond by typing 'cat' or 'dog') \n"))

def main():
  #if user answers dog they will be asked to pick a number to give them a different dog fact
  if answer == 'dog':
    dogfact = int(input("Please pick a number from 1 to 10 \n"))
    index = dogfact
    dapi = DogAPI.DogAPI(index=dogfact)
    results = dapi.get()
    print("Your dog fact is: " + results)

  #if user answers cat they will be asked a number 1-10 to give a different cat fact  
  elif answer == 'cat':
    catfact = int(input("Please pick a number from 1 to 10 \n"))
    id = catfact
    capi = CatAPI.CatAPI(id=catfact)
    results = capi.get()
    print("Your cat fact is: " + results)

  #in case someone does not give a proper answer  
  else:
    print("Please enter 'cat' or 'dog'")

main()