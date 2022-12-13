import requests

class CatAPI:
  def __init__(self, id=1):
    self.url = f'https://meowfacts.herokuapp.com/?id={id}'
    self.id = id
  def get(self):
    r = requests.get(self.url)
    response = r.json()

    if response.get('results'):
      return response['results']
    else:
      return None

  #change id updates id when the user will change it
  def change_id(self, id):
    self.id = id
    self.url = f'https://meowfacts.herokuapp.com/?id={id}'