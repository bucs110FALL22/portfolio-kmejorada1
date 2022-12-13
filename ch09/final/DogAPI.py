import requests

class DogAPI:
  def __init__(self, index=1):
    self.url = f'https://dog-facts-api.herokuapp.com/api/v1/resources/dogs?index={index}'
    self.index = index
  def get(self):
    r = requests.get(self.url)
    response = r.json()

    if response.get('results'):
      return response['results']
    else:
      return None
  #change index updates the index when the user changes it
  def change_index(self, index):
    self.index = index
    self.url = f'https://dog-facts-api.herokuapp.com/api/v1/resources/dogs?index={index}' 