import requests

APIkey = "CSubUG2QXR5ECIaeCoChAA==rXIcnOjUmlQ8eRLn"

muscle = 'biceps'
api_url = 'https://api.api-ninjas.com/v1/exercises?muscle={}'.format(muscle)
response = requests.get(api_url, headers={'X-Api-Key': APIkey})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)