import requests
import json

api_key='3k1D_aEzWYvwGrp78N3RZoopJBx2Ykv4ZnbQhi-Y0FdXfyyNmPP2Erslrl7ro0vraRjhT2ezaf7joVNm6bsxgHJ6yD7vSFUknMbrLs8bxDmaU5k_8pR478fZQFBeYHYx'
headers = {'Authorization': 'Bearer %s' % api_key}

url='https://api.yelp.com/v3/businesses/search'

# In the dictionary, term can take values like food, cafes or businesses like McDonalds
params = {'term':'indian','location':'98059', 'limit' : '5'}

# Making a get request to the API
req=requests.get(url, params=params, headers=headers)

# proceed only if the status code is 200
print('The status code is {}'.format(req.status_code))

# Making a get request to the API
req=requests.get(url, params=params, headers=headers)

# proceed only if the status code is 200
print('The status code is {}'.format(req.status_code))

# printing the text from the response 
json_object = json.loads(req.text)
# print(json.dumps(json_object, indent=1))

def loop_results():
  for x in json_object['businesses']:
    print(x['name'])

loop_results()

# async def search_result(param1, param2):
#   term = param1.activity.text
#   location = param2.activity.text
#   params = {'term' : term, 'location' : location, 'limit' : '5'}